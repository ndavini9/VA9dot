from abc import ABC, abstractmethod

from core.result import TestResult


class TestCase(ABC):

    id: str = ""
    name: str = ""
    title: str = ""

    category: str = "GENERAL"

    severity: str = "INFO"

    description: str = ""

    recommendation: str = ""

    cwe: list[str] = []
    cve: list[str] = []

    def validate(self):

        required = [
            "id",
            "name",
            "title"
        ]

        for field in required:
            if not getattr(self, field):
                raise ValueError(
                    f"{self.__class__.__name__}: missing {field}"
                )

    @abstractmethod
    def run(self, client) -> TestResult:
        pass
