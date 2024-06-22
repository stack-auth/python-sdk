import requests

class StackAuthClient:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.base_url = 'https://stackoverflow.com/oauth/'

    def get_authorization_url(self):
        return f"{self.base_url}authorize?client_id={self.client_id}&redirect_uri={self.redirect_uri}&scope=write_access"

    def get_access_token(self, code):
        url = f"{self.base_url}access_token"
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'code': code,
        }
        response = requests.post(url, params=params)
        return response.json().get('access_token')

    def refresh_access_token(self, refresh_token):
        url = f"{self.base_url}access_token"
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        response = requests.post(url, params=params)
        return response.json().get('access_token')
