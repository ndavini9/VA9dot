class TestResult:

    def __init__(
        self,
        test_id,
        name,
        status,
        severity,
        message
    ):
        self.test_id = test_id
        self.name = name
        self.status = status
        self.severity = severity
        self.message = message
