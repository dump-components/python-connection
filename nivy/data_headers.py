from system.operation_system import OperationSystem
from codification.encode import Encode


class DataHeaders:
    
    def __init__(self) -> None:
        self._os = OperationSystem()
        self._encoded_file = Encode()
        pass
    
    def header_get_task(self, token):
        return {'Authorization': f'Bearer {token}',
                'User-Agent': self._os.computer_name}
    
    def header_get_token(self):
        return {'User-Agent': self._os.computer_name}
    
    def data_error(self, messages_error):
        return {"messages": messages_error,
                "fatal_error": True}
    
    def header_default(self, token):
        return {'Authorization': f'Bearer {token}',
                'User-Agent': self._os.computer_name,
                'Content-Type': 'application/json'}
    
    def data_patch_files(self):
        data = {
            "files": {
                "name": "name_file",
                "base64_file": self._encoded_file.base64_encode("name_file"),
                "md5_hash": self._encoded_file.md5_hash("name_file"),
                "sha256_hash": self._encoded_file.sha256_hash("name_file")},
                "name": "name_file",
                "base64_file": self._encoded_file.base64_encode("name_file"),
                "md5_hash": self._encoded_file.md5_hash("name_file"),
                "sha256_hash": self._encoded_file.sha256_hash("name_file")}
        return data