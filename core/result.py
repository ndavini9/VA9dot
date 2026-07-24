class TestResult:

    def __init__(
        self,
        test_id,
        name=None,
        status=None,
        severity="INFO",
        message="",
        category=None,
        duration_ms=None,
        evidence=None,
        request=None,
        response=None,
        recommendation=None,
        cwe=None,
        cve=None
    ):

        self.test_id = test_id

        self.name = name or ""

        self.status = status or "UNKNOWN"

        self.severity = severity

        self.message = message

        self.category = category

        self.duration_ms = duration_ms

        self.evidence = evidence or {}

        self.request = request

        self.response = response

        self.recommendation = recommendation or ""

        self.cwe = cwe or []

        self.cve = cve or []


    def to_dict(self):

        return {
            "id": self.test_id,
            "name": self.name,
            "status": self.status,
            "severity": self.severity,
            "message": self.message,
            "category": self.category,
            "duration_ms": self.duration_ms,
            "evidence": self.evidence,
            "request": self.request,
            "response": self.response,
            "recommendation": self.recommendation,
            "cwe": self.cwe,
            "cve": self.cve
        }


    def __repr__(self):

        return (
            f"<TestResult "
            f"{self.test_id} "
            f"{self.status} "
            f"{self.severity}>"
        )
