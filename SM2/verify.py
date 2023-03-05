"""
签名验证部分
"""


from pysmx.SM2 import Verify
from .key_generator import get_pa
from .sign import sign


def verified(sign_info="你好", len_para=64):
    sig = sign(sign_info, len_para)
    pa = get_pa()
    print("verifying the sign and message")
    return Verify(sig, sign_info, pa, len_para)
