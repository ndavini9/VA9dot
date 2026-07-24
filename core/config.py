from pathlib import Path
import yaml


class Config:

    def __init__(self, filename="config.yaml"):

        self.filename = filename

        self.data = {}

        self.load()

    def load(self):

        cfg = Path(self.filename)

        if not cfg.exists():

            raise FileNotFoundError(f"Configuration file not found: {cfg}")

        with open(cfg, "r", encoding="utf-8") as f:

            self.data = yaml.safe_load(f)

    def get(self, key, default=None):

        parts = key.split(".")

        value = self.data

        for part in parts:

            if isinstance(value, dict):

                value = value.get(part)

            else:

                return default

            if value is None:

                return default

        return value

    @property
    def host(self):
        return self.get("target.host")

    @property
    def protocol(self):
        return self.get("target.protocol", "http")

    @property
    def port(self):
        return self.get("target.port", 80)

    @property
    def timeout(self):
        return self.get("http.timeout", 10)

    @property
    def verify_ssl(self):
        return self.get("http.verify_ssl", False)

    @property
    def username(self):
        return self.get("authentication.username")

    @property
    def password(self):
        return self.get("authentication.password")

    @property
    def output_directory(self):
        return self.get("report.output", "reports")

    @property
    def logging_directory(self):
        return self.get("logging.directory", "logs")