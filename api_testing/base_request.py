import json

import requests


class BaseRequest:

    def __init__(self, base_url, header=None):
        self.base_url = base_url
        self.header = header

    def send_request(self, url, method, data=None, expected_error_code=False,
                     expected_error_message=None):
        headers = self.header if self.header else None
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=headers)
        elif method == 'PUT':
            response = requests.put(url, json=data, headers=headers)
        elif method == 'PATCH':
            response = requests.patch(url, json=data, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f'Invalid HTTP method: {method}')

        if not (expected_error_code or expected_error_message) \
                and response.status_code not in (200, 201):
            raise ValueError(f'Invalid status code:'
                             f'{response.status_code}, {response.text}')

        return response

    def get(self, endpoint, object_id, expected_error_code=False,
            expected_error_message=None):
        url = f'{self.base_url}/{endpoint}/{object_id}'
        response = self.send_request(
            url,
            'GET',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        try:
            return response.json()  # Try to decode response body as JSON
        except json.JSONDecodeError:
            return {}

    def post(self, endpoint, object_id, data, expected_error_code=False,
             expected_error_message=None):
        url = f'{self.base_url}/{endpoint}/{object_id}'
        response = self.send_request(
            url,
            'POST',
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        return response

    def put(self, endpoint, object_id, data, expected_error_code=False,
            expected_error_message=None):
        url = f'{self.base_url}/{endpoint}/{object_id}'
        response = self.send_request(
            url,
            'PUT',
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        return response

    def patch(self, endpoint, object_id, data, expected_error_code=False,
              expected_error_message=None):
        url = f'{self.base_url}/{endpoint}/{object_id}'
        response = self.send_request(
            url,
            'PATCH',
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        return response.json()

    def delete(self, endpoint, object_id, expected_error_code=False,
               expected_error_message=None):
        url = f'{self.base_url}/{endpoint}/{object_id}'
        response = self.send_request(
            url,
            'DELETE',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        return response
