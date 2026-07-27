import argparse
import sys
import time

from core.config import Config
from core.context import ScanContext
from core.engine import Engine
from core.httpclient import HttpClient
from core.logger import Logger
from core.plugin_loader import PluginLoader
from core.report import ReportGenerator
from core.snmpclient import SnmpClient


def parse_args():

    parser = argparse.ArgumentParser(
        prog="va9dot",
        description="VA9dot - Vulnerability Assessment tool for internal products (API / SNMP / Web)."
    )

    parser.add_argument(
        "-c", "--config",
        default="config.yaml",
        help="Path to the configuration file (default: config.yaml)"
    )

    return parser.parse_args()


def main():

    args = parse_args()

    try:
        config = Config(args.config)
    except FileNotFoundError as ex:
        print(f"[VA9dot] {ex}", file=sys.stderr)
        return 2

    logger = Logger.get(config.logging_directory)

    logger.info("=" * 60)
    logger.info(
        "Starting VA9dot v%s",
        config.get("project.version", "0.0.0")
    )
    logger.info(
        "Target: %s://%s:%s",
        config.protocol,
        config.host,
        config.port
    )
    logger.info("=" * 60)

    scan_start = time.perf_counter()

    # ========================================================
    # Clients (HTTP always, SNMP only if enabled in config)
    # ========================================================
    http_client = None

    if config.http_enabled:

        http_client = HttpClient(
            protocol=config.protocol,
            host=config.host,
            port=config.port,
            username=config.username,
            password=config.password,
            timeout=config.timeout,
            verify_ssl=config.verify_ssl
        )

    snmp_client = None

    if config.snmp_enabled:

        snmp_client = SnmpClient(
            host=config.host,
            port=config.snmp_port,
            timeout=config.snmp_timeout,
            retries=config.snmp_retries,
            version=config.snmp_version
        )

        logger.info(
            "SNMP testing enabled (port %d, v%d)",
            config.snmp_port,
            config.snmp_version
        )

    context = ScanContext(
        config=config,
        http=http_client,
        snmp=snmp_client
    )

    # ========================================================
    # Load plugins
    # ========================================================
    loader = PluginLoader()
    tests = loader.load()

    logger.info("Tests loaded: %d", len(tests))

    # ========================================================
    # Engine
    # ========================================================
    engine = Engine(context)

    for test in tests:
        logger.info("Adding test: %s", test.id)
        engine.add_test(test)

    # ========================================================
    # Run scan
    # ========================================================
    results = engine.run()

    # ========================================================
    # Results (console / log summary)
    # ========================================================
    logger.info("=" * 60)
    logger.info("Scan results")
    logger.info("=" * 60)

    passed = 0
    failed = 0
    errors = 0

    for result in results:

        logger.info(
            "%s | %s | %s | %s",
            result.test_id,
            result.status,
            result.severity,
            result.message
        )

        if result.status == "PASS":
            passed += 1
        elif result.status == "FAIL":
            failed += 1
        elif result.status == "ERROR":
            errors += 1

        if getattr(result, "evidence", None):
            logger.info("Evidence: %s", result.evidence)

    elapsed = round((time.perf_counter() - scan_start) * 1000)

    logger.info("=" * 60)
    logger.info(
        "Summary: PASS=%d FAIL=%d ERROR=%d",
        passed,
        failed,
        errors
    )
    logger.info("Completed in %d ms", elapsed)
    logger.info("=" * 60)

    # ========================================================
    # Reports
    # ========================================================
    want_html = config.get("report.html", True)
    want_json = config.get("report.json", True)

    if want_html or want_json:

        report = ReportGenerator(
            output_directory=config.output_directory
        )

        if want_html:
            path = report.generate_html(results)
            logger.info("HTML report written to %s", path)

        if want_json:
            path = report.generate_json(results)
            logger.info("JSON report written to %s", path)

    # Non-zero exit code if anything failed or errored: useful for CI/cron.
    return 1 if (failed or errors) else 0


if __name__ == "__main__":
    sys.exit(main())
