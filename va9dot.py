import argparse

from core.config import Config
from core.httpclient import HttpClient
from core.engine import Engine
from core.plugin_loader import PluginLoader
from core.report import ReportGenerator


parser = argparse.ArgumentParser()


parser.add_argument(
    "--host",
    required=True
)


parser.add_argument(
    "--user",
    required=True
)


parser.add_argument(
    "--password",
    required=True
)


args = parser.parse_args()



cfg = Config()

client = HttpClient(
    protocol=cfg.protocol,
    host=cfg.host,
    port=cfg.port,
    username=cfg.username,
    password=cfg.password,
    timeout=cfg.timeout,
    verify_ssl=cfg.verify_ssl
)



engine = Engine(client)



loader = PluginLoader()


tests = loader.load()



for test in tests:

    engine.add_test(test)



results = engine.run()



for result in results:

    result.status = (
        "PASS"
        if result.passed
        else
        "FAIL"
    )

    print(
        f"[{result.status}] "
        f"{result.id} "
        f"{result.message}"
    )



report = ReportGenerator()


filename = report.generate(
    results
)


print()

print(
    "Report generated:"
)

print(filename)
