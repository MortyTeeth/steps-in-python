from enum import Enum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        status_codes = ["информация", "успех", "перенаправление", "ошибка клиента", "ошибка сервера"]
        http_status_codes = dict(zip(HTTPStatusCodes, status_codes))
        return http_status_codes[self]
