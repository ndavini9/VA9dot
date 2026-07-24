from core.testcase import TestCase
from core.result import TestResult


class DiscoveryTest(TestCase):

    id = "DISC-001"

    title = "HTTP Reachability"

    severity = "INFO"

    recommendation = (
        "Verify HTTP service availability."
    )


    def run(self, client):

        try:

            result = client.get("/")

            response = result["response"]


            return TestResult(

                id=self.id,

                title=self.title,

                severity=self.severity,

                passed=response.status_code < 500,

                duration_ms=result["duration_ms"],

                message=(
                    f"HTTP {response.status_code}"
                ),

                request=str(
                    result["request"]
                ),

                response=str(
                    dict(response.headers)
                ),

                recommendation=self.recommendation

            )


        except Exception as ex:

            return TestResult(

                id=self.id,

                title=self.title,

                severity="CRITICAL",

                passed=False,

                message=str(ex),

                recommendation=(
                    "Check network connectivity."
                )

            )