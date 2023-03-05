from SM2.encryption import encrypt
from SM2.decryption import decrypt


if __name__ == '__main__':
    # SM2算法
    s = input("input the string to be encrypted: ")
    encrypted_message = encrypt(s)
    print("the encrypted message is " + str(encrypted_message))
    decrypted_message = decrypt(encrypted_message)
    print("decrypting...")
    print("the decrypted message is " + str(decrypted_message))
