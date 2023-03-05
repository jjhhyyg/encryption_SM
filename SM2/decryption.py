"""
解密部分
"""


from pysmx.SM2 import Decrypt
from .key_generator import get_da


def decrypt(encrypted_message, len_para=64):
    da = get_da()
    decrypted_message = Decrypt(encrypted_message, da, len_para)
    return decrypted_message
