
class AuthError(Exception):
    pass

class AccessTokenError(AuthError):
    pass

class APIError(AuthError):
    pass
