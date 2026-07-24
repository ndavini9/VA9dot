from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class TestResult:

    test_id: str
    name: str
    status: str
    severity: str
    message: str

    duration: int = 0

    recommendation: str = ""

    request: object = None

    response: object = None

    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


# Alias temporaneo per compatibilità con il refactoring
Result = TestResult