"""
密钥生成部分
"""


from pysmx.SM2 import generate_keypair

PA, DA = generate_keypair()
print("generating public key and private key...")


def get_pa():
    print("get the public key: " + str(PA))
    return PA


def get_da():
    print("get the private key: " + str(DA))
    return DA
