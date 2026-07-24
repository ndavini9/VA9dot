class TestGenerator:

    def __init__(self, endpoints):

        self.endpoints = endpoints

    def generate(self):

        tests = []

        for endpoint in self.endpoints:

            tests.append(AuthenticationTest(endpoint))

            tests.append(MethodTest(endpoint))

            tests.append(HeaderTest(endpoint))

            tests.append(ParameterTest(endpoint))

        return tests