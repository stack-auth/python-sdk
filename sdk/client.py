import requests

class AuthClient:
    def __init__(self, client_id, client_secret, redirect_uri, auth_base_url, token_url, scope=''):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.auth_base_url = auth_base_url
        self.token_url = token_url
        self.scope = scope

    def get_authorization_url(self):
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'response_type': 'code'
        }
        return f"{self.auth_base_url}/authorize", params

    def get_access_token(self, code):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'code': code,
            'grant_type': 'authorization_code'
        }
        response = requests.post(self.token_url, data=data)
        return response.json().get('access_token')

    def refresh_access_token(self, refresh_token):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        response = requests.post(self.token_url, data=data)
        return response.json().get('access_token')
