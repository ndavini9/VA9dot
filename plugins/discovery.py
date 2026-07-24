from core.testcase import TestCase
from core.result import TestResult


class DiscoveryTest(TestCase):

    id = "DISC-001"

    name = "HTTP Reachability"

    title = "HTTP service availability check"

class DiscoveryTest(TestCase):

    id = "DISC-001"

    name = "HTTP Reachability"

    title = "HTTP Service Availability Check"

    category = "DISCOVERY"

    severity = "INFO"

    recommendation = (
        "Verify HTTP service availability."
    )


    def run(self, client):

        try:

            result = client.get("/")

            response = result["response"]

            status = (
                "PASS"
                if response.status_code < 500
                else "FAIL"
            )


          return TestResult(

    test_id=self.id,

    name=self.name,

    status="ERROR",

    severity="INFO",

    category=self.category,

    message=str(ex),

    recommendation=(
        "Check network connectivity "
        "and HTTP service availability."
    )

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
                    "Check network connectivity "
                    "and HTTP service availability."
                )

            )

    category = "DISCOVERY"

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

                status=(
                    "PASS"
                    if response.status_code < 500
                    else "FAIL"
                ),

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

                severity="INFO",

                status="ERROR",

                message=str(ex),

                recommendation=(
                    "Check network connectivity."
                )

            )
