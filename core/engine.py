import time

from core.logger import Logger
from core.plugin_loader import PluginLoader
from core.engine import Engine
from core.http_client import HttpClient


logger = Logger.get()


def main():

    logger.info("=" * 60)
    logger.info("Starting VA9dot")
    logger.info("=" * 60)


    scan_start = time.perf_counter()


    # ---------------------------------------------------------
    # Configuration
    # ---------------------------------------------------------

    protocol = "http"
    host = "192.168.1.1"
    port = 80

    username = None
    password = None


    # ---------------------------------------------------------
    # Create HTTP client
    # ---------------------------------------------------------

    client = HttpClient(

        protocol=protocol,

        host=host,

        port=port,

        username=username,

        password=password

    )


    # ---------------------------------------------------------
    # Load plugins
    # ---------------------------------------------------------

    loader = PluginLoader()

    tests = loader.load()


    logger.info(
        "Tests loaded: %d",
        len(tests)
    )


    # ---------------------------------------------------------
    # Initialize engine
    # ---------------------------------------------------------

    engine = Engine(
        client
    )


    for test in tests:

        engine.add_test(
            test
        )


    # ---------------------------------------------------------
    # Run scan
    # ---------------------------------------------------------

    results = engine.run()


    # ---------------------------------------------------------
    # Results
    # ---------------------------------------------------------

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


        if result.evidence:

            logger.info(

                "Evidence: %s",

                result.evidence

            )


    elapsed = round(

        (time.perf_counter() - scan_start) * 1000

    )


    logger.info("=" * 60)

    logger.info(

        "Summary: PASS=%d FAIL=%d ERROR=%d",

        passed,

        failed,

        errors

    )


    logger.info(

        "Completed in %d ms",

        elapsed

    )


    logger.info("=" * 60)



if __name__ == "__main__":

    main()
