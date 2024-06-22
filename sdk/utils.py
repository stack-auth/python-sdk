import requests
from .exceptions import APIError

def make_request(url, method='GET', params=None, headers=None, data=None):
    try:
        response = requests.request(method, url, params=params, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise APIError(f"Error making {method} request to {url}: {e}")
