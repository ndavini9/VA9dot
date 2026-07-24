import requests
import time


class HttpClient:

    def __init__(
        self,
        protocol,
        host,
        port,
        username=None,
        password=None,
        timeout=10,
        verify_ssl=False
    ):

        self.protocol = protocol
        self.host = host
        self.port = port

        self.base_url = (
            f"{protocol}://{host}:{port}"
        )

        self.timeout = timeout

        self.verify_ssl = verify_ssl

        self.session = requests.Session()


        if username and password:

            self.session.auth = (
                username,
                password
            )


    def request(
        self,
        method,
        path,
        json=None,
        data=None,
        headers=None
    ):

        url = self.base_url + path

        start = time.perf_counter()


        response = self.session.request(

            method=method,

            url=url,

            json=json,

            data=data,

            headers=headers,

            timeout=self.timeout,

            verify=self.verify_ssl,

            allow_redirects=True

        )


        elapsed = (
            time.perf_counter() - start
        ) * 1000


        return {

            "response": response,

            "duration_ms": round(
                elapsed,
                2
            ),

            "request": {

                "method": method,

                "url": url,

                "json": json

            }

        }


    def get(
        self,
        path,
        **kwargs
    ):

        return self.request(

            "GET",

            path,

            **kwargs

        )


    def post(
        self,
        path,
        **kwargs
    ):

        return self.request(

            "POST",

            path,

            **kwargs

        )


    def put(
        self,
        path,
        **kwargs
    ):

        return self.request(

            "PUT",

            path,

            **kwargs

        )


    def delete(
        self,
        path,
        **kwargs
    ):

        return self.request(

            "DELETE",

            path,

            **kwargs

        )
