from abc import ABC, abstractmethod

from core.result import TestResult


class TestCase(ABC):

    id = ""
    name = ""
    title = ""

    severity = "INFO"

    recommendation = ""

    @abstractmethod
    def run(self, client) -> TestResult:
        pass