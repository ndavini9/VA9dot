import logging
import time

from core.logger import Logger
from core.plugin_loader import PluginLoader
from core.engine import Engine
from core.httpclient import HttpClient


# ============================================================
# Logging configuration
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger(__name__)


# ============================================================
# Main
# ============================================================

def main():

    logger.info("=" * 60)
    logger.info("Starting VA9dot")
    logger.info("=" * 60)


    start_time = time.time()


    # --------------------------------------------------------
    # Load plugins
    # --------------------------------------------------------

    loader = PluginLoader()

    tests = loader.load()


    logger.info(
        "Tests loaded: %s",
        len(tests)
    )


    if not tests:

        logger.warning(
            "No tests available"
        )

        return


    # --------------------------------------------------------
    # Execute scan
    # --------------------------------------------------------

    engine = Engine(
        tests
    )


    results = engine.run()


    # --------------------------------------------------------
    # Results
    # --------------------------------------------------------

    logger.info("=" * 60)
    logger.info("Scan results")
    logger.info("=" * 60)


    for result in results:


        logger.info(
            "%s | %s | %s | %s",
            result.test_id,
            result.status,
            result.severity,
            result.message
        )


        if result.evidence:

            logger.info(
                "Evidence: %s",
                result.evidence
            )


    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    elapsed = (
        time.time()
        - start_time
    )


    passed = len(
        [
            r for r in results
            if r.status == "PASS"
        ]
    )

    failed = len(
        [
            r for r in results
            if r.status == "FAIL"
        ]
    )

    errors = len(
        [
            r for r in results
            if r.status == "ERROR"
        ]
    )


    logger.info("=" * 60)

    logger.info(
        "Summary: PASS=%s FAIL=%s ERROR=%s",
        passed,
        failed,
        errors
    )

    logger.info(
        "Completed in %.2f seconds",
        elapsed
    )

    logger.info("=" * 60)



if __name__ == "__main__":

    main()
