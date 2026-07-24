import logging
from pathlib import Path
from datetime import datetime


class Logger:

    _instance = None

    @classmethod
    def get(cls, directory="logs"):

        if cls._instance is not None:
            return cls._instance

        Path(directory).mkdir(parents=True, exist_ok=True)

        logfile = Path(directory) / f"{datetime.now():%Y%m%d}.log"

        logger = logging.getLogger("VA9dot")

        logger.setLevel(logging.INFO)

        logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            "%H:%M:%S"
        )

        fh = logging.FileHandler(logfile, encoding="utf-8")
        fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        cls._instance = logger

        return logger