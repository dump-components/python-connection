from .nivy import Nivy

class SearchContent:
    
    
    def __init__(self) -> None:
        self.__api = Nivy()
        self.__content= self.__api.authorization().get_content()

    @property
    def content(self):
        return (self.__api.token, self.__content)