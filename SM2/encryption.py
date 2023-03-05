"""
加密部分
"""


from pysmx.SM2 import Encrypt
from .key_generator import get_pa


def encrypt(message, len_para=64):
    pa = get_pa()
    encrypted_message = Encrypt(message, pa, len_para, 0)  # 此处的1代表e是否是16进制字符串
    return encrypted_message
