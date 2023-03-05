from SM2.encryption import encrypt
from SM2.decryption import decrypt

import json

if __name__ == '__main__':
    with open('./configuration_json_file/configuration.json', encoding='utf-8') as f:
        config_json = json.load(f)
        # 将json对象转换为str对象，便于加密
        config_str = json.dumps(config_json, indent=2)
        print(config_str)

    # SM2算法
    s = config_str
    encrypted_message = encrypt(s)
    print("the encrypted message is " + str(encrypted_message))
    decrypted_message = decrypt(encrypted_message)
    print("decrypting...")
    print("the decrypted message is " + decrypted_message.decode('utf-8'))
