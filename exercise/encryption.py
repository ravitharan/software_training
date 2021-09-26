import os.path
import base64

def encrypt_credential():
    """ convert credentials.json file into encrypted binary file credentials.bin
    PROCEDURE:
    1) Read all contents of credentials.json and save into a string variable.
    2) Convert the string into bytes by encode()
    3) Using xor operator convert each byte into another byte value.
    4) Save the new bytes content into a binary file credentials.bin
    """

    credential = ''
    with open('credentials.json','r') as f:
        data = f.read()

        #encrypt
        data_bytes = data.encode('ascii')
        base64_bytes = base64.b64encode(data_bytes)
        base64_data = base64_bytes.decode('ascii')

        #encode with xor
        xorKey = 'K';
        length = len(base64_bytes);

        for i in range(length):
            base64_data = (base64_data[:i] +
                         chr(ord(base64_data[i]) ^ ord(xorKey)) +
                         base64_data[i + 1:]);
        #convert to bytes  
        credential = base64_data.encode('ascii')    

    #bin file
    with open('credentials.bin','wb') as f:
         f.write(credential)

         

def decrypt_credential():
    """ convert credentials.bin file into credentials.json file """

    credential=''
    with open('credentials.bin','rb') as f:
        data = f.read()
        
        #convert to string
        data = data.decode('ascii')

        #decode with XOR
        xorKey = 'K';
        length = len(data);

        for i in range(length):
            data = (data[:i] +
                        chr(ord(data[i]) ^ ord(xorKey)) +
                        data[i + 1:]);
        #decrypt  
        base64_bytes = data.encode('ascii')
        decode_bytes = base64.b64decode(base64_bytes)
        credential = decode_bytes.decode('ascii')


    #json file
    with open('credentials.json','w') as f:
         f.write(credential)

if __name__ == '__main__':
    encrypt_credential()
    #decrypt_credential()

