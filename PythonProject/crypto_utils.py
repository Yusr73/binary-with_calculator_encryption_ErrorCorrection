from Crypto.Cipher import AES


KEY = b'ThisIsASecretKey'

def pad(data):
    padding = 16 - len(data) % 16
    return data + bytes([padding] * padding)

def unpad(data):
    padding = data[-1]
    return data[:-padding]

def encrypt_json_string(json_str):
    data = json_str.encode('utf-8')
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data))
    return cipher.iv + ct_bytes

def decrypt_to_json_string(cipher_data):
    iv = cipher_data[:16]
    ct = cipher_data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct))
    return pt.decode('utf-8')
