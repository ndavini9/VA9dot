from core.testcase import TestCase
from core.result import TestResult


class HeaderSecurityTest(TestCase):

    id = "HTTP-001"

    name = "Security Headers"

    title = "HTTP Security Headers Configuration"

    category = "WEB"

    severity = "MEDIUM"

    cwe = [
        "CWE-693"
    ]

    recommendation = (
        "Configure missing HTTP security headers."
    )


    required_headers = [
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Content-Security-Policy"
    ]


    def run(self, client):

        try:

            result = client.get("/")

            response = result["response"]


            existing_headers = [
                h.lower()
                for h in response.headers.keys()
            ]


            missing = []

            for header in self.required_headers:

                if header.lower() not in existing_headers:

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


        except Exception as ex:

            return TestResult(

                id=self.id,

                title=self.title,

                severity="INFO",

                passed=False,

                message=str(ex)

            )
