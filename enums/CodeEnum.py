"""
对应接口的enum信息
"""

from enum import Enum

class RESP_CODE_ENUM(Enum):
    '''
    接口返回的Code信息
    '''
    def __str__(self):
        return str(self.value)

    SUCCESS = '0000'
    SERVER_ERROR = '9999'