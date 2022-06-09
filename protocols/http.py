import requests, json
from requests import Response

class HTTP:


    def get(self, route, headers, auth=None) -> Response:
        return requests.get(url=route, headers=headers, auth=auth)

    def post(self, route: str, data, headers) -> Response:
        return requests.post(url=route, data=json.dumps(data), headers=headers)

    def patch(self, route: str, data, headers) -> Response:
        return requests.patch(url=route, data=json.dumps(data), headers=headers)
