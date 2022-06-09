from abc import ABC, abstractmethod

class OauthABC(ABC):
    
    def __init__(self) -> None:
        self._username = str
        self._password = str
        self._oauth = tuple
    
    @property
    @abstractmethod
    def username(self):
        pass
    
    @property
    @abstractmethod
    def password(self):
        pass
    
    @property
    @abstractmethod
    def oauth(self):
        pass

