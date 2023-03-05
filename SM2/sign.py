"""
签名部分
"""


from pysmx.SM2 import Sign
from .key_generator import get_da
from random import randint


def sign(sign_info="你好", len_para=64):
    da = get_da()
    sig = Sign(sign_info, da, str(randint(0, int(1e9))), len_para)
    return sig
