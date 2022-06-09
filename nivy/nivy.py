import sys

from requests import Response
from ..authorization.oauth import Oauth
from ..protocols.http import HTTP
from .nivy_routes import NivyRoutes
from ..protocols.status_code_enum import StatusCode
from .data_headers import DataHeaders
from exceptions.logger import Logger

class Nivy(HTTP):

    def __init__(self) -> None:
        super().__init__()
        self.log = Logger()
        self._data_headers = DataHeaders()

    @property
    def token(self):
        return self._token
    
    def authorization(self):
        self.log.info("iniciando autenticacao com API Nivy")
        try:
            response = self.get(route=NivyRoutes.authorization.value, auth=Oauth().oauth, headers=self._data_headers.header_get_token())
            self.log.debug(response)
        except Exception as err:
            raise self.log.critical(err)
        self._token = response.json()
        self.log.debug(f"autenticacao com API Nivy TOKEN: {self._token}")
        self.log.debug(response)
        return self

    def get_content(self):
        self.log.info("fazendo requisição para API")
        try:
            response = self.get(route=NivyRoutes.get.value, headers=self._data_headers.header_get_task(token=self._token))
        except Exception as err:
            raise self.log.critical(err)
        self.log.debug(response)
        self.log.debug(response.content)
        self._task_response_have_content(response)
        return response.json()
    
    def post_error(self, id, token, messages_error: str):
        self.log.info("fazendo requisição para API para enviar um erro")
        try:
            response = self.post(route=NivyRoutes.error.value.replace("#", id), headers=self._data_headers.header_default(token), data=self._data_headers.data_error(messages_error))
        except Exception as err:
            raise self.log.critical(err)
        self.log.debug(f"resposta: {response}")
        self.log.debug(response.content)
        return response.json()
    
    def patch_file(self, id, token, fap, fgts):
        self.log.info("fazendo requisição para API para enviar os dados")
        try:
            response = self.patch(route=NivyRoutes.patch.value + id, headers=self._data_headers.header_default(token), data=self._data_headers.data_patch_files(fap, fgts))
        except Exception as err:
            raise self.log.critical(err)
        self.log.debug(f"resposta: {response}")
        self.log.debug(response.content)
        return response.json()
    
    def _task_response_have_content(self, task_response: Response):
        self.log.info("verificando se a resposta contem um conteudo")
        try:
            response_status_code = task_response.status_code
        except Exception as err:
            raise self.log.critical(err)
        self._valid_status_code(response_status_code)
        return task_response.content
    
    def _valid_status_code(self, response_status_code):
        if  response_status_code != StatusCode.accepted.value:
            sys.exit(self.log.debug(self._associate_status_code(response_status_code)))
        self.log.info(self._associate_status_code(response_status_code))
    
    def _associate_status_code(self, status_code):
        associate = {
            StatusCode.created.value: "Created",
            StatusCode.accepted.value: "Accepted",
            StatusCode.no_content.value: "No content",
            StatusCode.error_client.value: "Error client",
            StatusCode.redirect.value: "Redirect",
            StatusCode.not_found.value: "Not Found"
        }
        return associate.get(status_code, "não reconhecemos esse status code como valido")