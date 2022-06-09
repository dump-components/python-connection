from .oauth_abc import OauthABC
from system.enviroments import Enviroments

class Oauth(OauthABC):
    
    
    def __init__(self) -> None:
        self._username_api = Enviroments.username_api.value
        self._password_api = Enviroments.password_api.value
        self._oauth = self.default()
    
    @property
    def username(self):
        return self._username_api
    
    @property
    def password(self):
        return self._password_api

    @property
    def oauth(self):
        return self._oauth
    
    def default(self):
        return (self._username_api, self._password_api)