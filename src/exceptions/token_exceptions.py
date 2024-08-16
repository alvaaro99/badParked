class AccessTokenRequired(Exception):
    'User has provided a refresh token when an access token is needed'
    pass


class RefreshTokenRequired(Exception):
    'User has provided an access token when a refresh token is needed'
    pass

class InvalidToken(Exception):
    'User has provided an invalid or expired token'
    pass