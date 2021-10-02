import os.path
import base64
import random

def encrypt_credential():
    """ convert credentials.json file into encrypted binary file credentials.bin
    PROCEDURE:
    1) Read all contents of credentials.json and save into a string variable.
    2) Convert the string into bytes by encode()
    3) Using xor operator convert each byte into another byte value.
    4) Save the new bytes content into a binary file credentials.bin
    """

    with open('credentials.json','r') as f:
        data = f.read().encode()

        keys = random.sample(range(256), 8)
        print(keys)
        encode_keys = base64.b64encode(bytes(keys))
        print(encode_keys)
        hidden_keys = []
        for k in encode_keys:
            hidden_keys.append(k ^ b'k'[0])
        print(hidden_keys)
        
        bin_data = []
        for i, d in enumerate(data):
            bin_data.append(d ^ keys[i%8])


        #bin file
        with open('credentials.bin','wb') as f:
            key_len = len(hidden_keys)
            f.write(key_len.to_bytes(1, 'little'))
            f.write(bytes(hidden_keys))
            f.write(bytes(bin_data))

         

def decrypt_credential():
    """ convert credentials.bin file into credentials.json file """

    with open('credentials.bin','rb') as f:
        data = f.read()
        key_len = data[0]
        hidden_keys = data[1:key_len+1]
        print(list(hidden_keys))
        encode_keys = []
        for k in hidden_keys:
            encode_keys.append(k ^ b'k'[0])
        encode_keys = bytes(encode_keys)
        print(encode_keys)
        keys = base64.b64decode(encode_keys)
        print(list(keys))
        
        credential = []
        for i, d in enumerate(data[key_len+1:]):
            credential.append(d ^ keys[i%8])
        credential = bytes(credential)

        with open('credentials.json', 'w') as f:
             f.write(credential.decode())

if __name__ == '__main__':
    encrypt_credential()
    decrypt_credential()

