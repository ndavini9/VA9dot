from core.testcase import TestCase
from core.result import TestResult


class DiscoveryTest(TestCase):

    id = "DISC-001"

    name = "HTTP Reachability"

    title = "HTTP Service Availability Check"

    category = "DISCOVERY"

    severity = "INFO"

    recommendation = (
        "Verify HTTP service availability."
    )


    def run(self, context):

        try:

            result = context.http.get("/")

            response = result["response"]


            status = (
                "PASS"
                if response.status_code < 500
                else "FAIL"
            )


            return TestResult(

                test_id=self.id,

                name=self.name,

                status=status,

                severity=self.severity,

                category=self.category,

                duration_ms=result.get(
                    "duration_ms"
                ),

                message=(
                    f"HTTP {response.status_code}"
                ),

                evidence={
                    "status_code":
                        response.status_code
                },

                request=str(
                    result.get("request")
                ),

                response=str(
                    dict(response.headers)
                ),

                recommendation=self.recommendation

            )


        except Exception as ex:


            return TestResult(

                test_id=self.id,

                name=self.name,

                status="ERROR",

                severity="INFO",

                category=self.category,

                message=str(ex),

                recommendation=(
                    "Check HTTP connectivity."
                )

            )
