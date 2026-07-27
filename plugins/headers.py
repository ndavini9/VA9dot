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


    def run(self, context):

        try:

            result = context.http.get("/")

            response = result["response"]


            existing_headers = [

                header.lower()

                for header in response.headers.keys()

            ]


            missing = []


            for header in self.required_headers:

                if header.lower() not in existing_headers:

                    missing.append(header)


            passed = len(missing) == 0


            return TestResult(

                test_id=self.id,

                name=self.name,

                status=(
                    "PASS"
                    if passed
                    else "FAIL"
                ),

                severity=self.severity,

                category=self.category,

                duration_ms=result["duration_ms"],

                message=(

                    "All headers present"

                    if passed

                    else

                    f"Missing: {missing}"

                ),

                evidence={

                    "missing_headers": missing,

                    "checked_headers": (
                        self.required_headers
                    )

                },

                recommendation=self.recommendation,

                cwe=self.cwe

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
                    "Check HTTP service availability."
                )

            )
