import time

from core.logger import Logger
from core.result import TestResult


class Engine:

    def __init__(self, client):

        self.client = client
        self.tests = []
        self.logger = Logger.get()


    def add_test(self, test):

        self.tests.append(test)


    def run(self):

        results = []

        total = len(self.tests)

        self.logger.info("=" * 60)
        self.logger.info("Starting scan")
        self.logger.info(
            "Tests loaded: %d",
            total
        )
        self.logger.info("=" * 60)


        scan_start = time.perf_counter()


        for index, test in enumerate(
            self.tests,
            start=1
        ):

            self.logger.info(
                "[%d/%d] Executing %s",
                index,
                total,
                test.id
            )


            start = time.perf_counter()


            try:

                result = test.run(
                    self.client
                )


                if hasattr(
                    result,
                    "duration_ms"
                ):

                    result.duration_ms = round(
                        (time.perf_counter() - start)
                        * 1000
                    )


                results.append(result)


            except Exception as ex:

                self.logger.exception(ex)


                results.append(

                    TestResult(

                        test_id=test.id,

                        name=getattr(
                            test,
                            "name",
                            test.id
                        ),

                        status="ERROR",

                        severity="HIGH",

                        message=str(ex)

                    )

                )


        total_time = round(
            (time.perf_counter() - scan_start)
            * 1000
        )


        self.logger.info(
            "Scan completed in %d ms",
            total_time
        )


        return results
