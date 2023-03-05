"""
密钥生成部分
"""


from pysmx.SM2 import generate_keypair

PA, DA = generate_keypair()


def get_pa():
    return PA


def get_da():
    return DA
