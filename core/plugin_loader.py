import os
import importlib
import inspect

from core.testcase import TestCase


class PluginLoader:


    def __init__(self, directory="plugins"):

        self.directory = directory


    def load(self):

        tests = []

        base_path = os.path.abspath(
            self.directory
        )

        print("Plugin directory:")
        print(base_path)


        if not os.path.exists(base_path):

            print("Plugin directory not found")

            return tests


        for file in os.listdir(base_path):

            if not file.endswith(".py"):
                continue

            if file.startswith("__"):
                continue


            module_name = (
                f"{self.directory}.{file[:-3]}"
            )


            print(
                "Loading plugin:",
                module_name
            )


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

                    print(
                        "Test found:",
                        obj.id
                    )

                    tests.append(obj())


        print(
            "Plugins loaded:",
            len(tests)
        )


        return tests