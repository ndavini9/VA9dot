import json
import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader


class ReportGenerator:

    def __init__(
        self,
        output_directory="reports",
        template_directory="templates"
    ):

        self.output_directory = output_directory

        self.environment = Environment(
            loader=FileSystemLoader(template_directory)
        )

        self._timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def _summary(self, results):

        summary = {"PASS": 0, "FAIL": 0, "ERROR": 0, "SKIPPED": 0}

        for result in results:
            summary[result.status] = summary.get(result.status, 0) + 1

        return summary

    def generate_html(self, results):

        template = self.environment.get_template("report.html")

        os.makedirs(self.output_directory, exist_ok=True)

        filename = os.path.join(
            self.output_directory,
            f"VA9dot_{self._timestamp}.html"
        )

        html = template.render(
            results=results,
            summary=self._summary(results),
            date=datetime.now()
        )

        with open(filename, "w", encoding="utf-8") as file:
            file.write(html)

        return filename

    def generate_json(self, results):

        os.makedirs(self.output_directory, exist_ok=True)

        filename = os.path.join(
            self.output_directory,
            f"VA9dot_{self._timestamp}.json"
        )

        payload = {
            "generated": datetime.now().isoformat(),
            "summary": self._summary(results),
            "results": [result.to_dict() for result in results]
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(payload, file, indent=2, ensure_ascii=False, default=str)

        return filename
