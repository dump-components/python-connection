from enum import Enum
from system.enviroments import Enviroments

class NivyRoutes(Enum):
    
    host = Enviroments.host_api_nivy.value
    authorization = host + '/api/tokens/criar'
    error = host + '/api/tarefas/#/erros'
    patch = host + '/api/tarefas/conectividade-social/'
    get = host + '/api/tarefas/conectividade-social/proxima-pendente'
    