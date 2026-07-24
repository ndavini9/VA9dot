import os
import importlib
import inspect
import logging

from core.testcase import TestCase


logger = logging.getLogger(__name__)


class PluginLoader:


    def __init__(self, directory="plugins"):

        self.directory = directory


    def load(self):

        tests = []

        if not os.path.exists(self.directory):

            logger.error(
                "Plugin directory missing"
            )

            return tests


        for file in os.listdir(self.directory):

            if not file.endswith(".py"):
                continue

            if file.startswith("__"):
                continue


            module_name = (
                f"{self.directory}.{file[:-3]}"
            )


            try:

                module = importlib.import_module(
                    module_name
                )


                for _, obj in inspect.getmembers(
                    module,
                    inspect.isclass
                ):


                    if (
                        issubclass(obj, TestCase)
                        and obj != TestCase
                    ):

                        instance = obj()

                        instance.validate()

                        tests.append(
                            instance
                        )


            except Exception as e:

                logger.error(
                    "%s failed: %s",
                    module_name,
                    e
                )


        return tests
