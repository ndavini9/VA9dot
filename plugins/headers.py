from core.testcase import TestCase
from core.result import TestResult


class HeaderSecurityTest(TestCase):

    id = "HTTP-001"

    title = "Security Headers"

    severity = "MEDIUM"

    recommendation = (
        "Configure missing HTTP security headers."
    )


    required_headers = [
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]


    def run(self, client):

        result = client.get("/")

        response = result["response"]

        missing = []

        for header in self.required_headers:

            if header not in response.headers:

                missing.append(header)


        passed = len(missing) == 0


        return TestResult(

            id=self.id,

            title=self.title,

            severity=self.severity,

            passed=passed,

            duration_ms=result["duration_ms"],

            message=(
                "All headers present"
                if passed
                else
                f"Missing: {missing}"
            ),

            recommendation=self.recommendation

        )