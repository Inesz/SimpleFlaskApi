from enum import Enum


class SimpleEqualEnum(Enum):
    def __eq__(self, cmp):
        if isinstance(cmp, str):
            return self.value == cmp
        else:
            super.__eq__(cmp)


class HttpMethod(SimpleEqualEnum):
    POST = "POST"
    GET = "GET"
