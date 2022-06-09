from enum import Enum


class StatusCode(Enum):
    
    created = 200
    no_content = 204
    accepted = 202
    error_client = 422
    redirect = 302
    not_found = 404