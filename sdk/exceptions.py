
class StackAuthError(Exception):
    pass

class AccessTokenError(StackAuthError):
    pass

class APIError(StackAuthError):
    pass
