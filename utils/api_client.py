import requests


class APIClient:

    def get(self, url, params=None, headers=None):
        response = requests.get(
            url,
            params=params,
            headers=headers
        )
        return response

    def post(self, url, data=None, headers=None):
        response = requests.post(
            url,
            json=data,
            headers=headers
        )
        return response

    def put(self, url, data=None, headers=None):
        response = requests.put(
            url,
            json=data,
            headers=headers
        )
        return response

    def delete(self, url, headers=None):
        response = requests.delete(
            url,
            headers=headers
        )
        return response

    def patch(self, url, data=None, headers=None):
        response = requests.patch(
            url,
            json=data,
            headers=headers
        )

        return response

    def get_with_auth(self, url, username, password):
        response = requests.get(
            url,
            auth=(username, password)
        )

        return response

    def get_with_token(self, url, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(
            url,
            headers=headers
        )

        return response

    def assert_status(self, response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected status {expected_status}, "
            f"but got {response.status_code}"
        )

    def get_json(self, response):
        return response.json()

    def assert_json_value(self, response, key, expected_value):
        data = response.json()

        assert key in data, (
            f"Key '{key}' not found in response. "
            f"Available keys: {list(data.keys())}"
        )

        assert data[key] == expected_value, (
            f"Expected {key}={expected_value}, "
            f"but got {data[key]}"
        )