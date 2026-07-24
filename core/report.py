from datetime import datetime

from jinja2 import Environment, FileSystemLoader

import os


class ReportGenerator:


    def __init__(self):

        self.environment = Environment(
            loader=FileSystemLoader(
                "templates"
            )
        )


    def generate(self, results):

        template = self.environment.get_template(
            "report.html"
        )


        filename = (
            "reports/"
            "VA9dot_"
            + datetime.now()
            .strftime("%Y%m%d_%H%M%S")
            + ".html"
        )


        os.makedirs(
            "reports",
            exist_ok=True
        )


        html = template.render(
            results=results,
            date=datetime.now()
        )


        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)


        return filename