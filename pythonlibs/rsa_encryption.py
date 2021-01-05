from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
from requests.utils import quote


def rsa_encrypt(value, key, url_encode=False):
    rsa_key = RSA.importKey(base64.b64decode(key))
    cipher = PKCS1_v1_5.new(rsa_key)
    encrypted = base64.b64encode(cipher.encrypt(value.encode("utf8")))
    if url_encode:
        return quote(encrypted, safe='')
    return encrypted


def rsa_decrypt(value, private_key):
    encrypted_message = base64.b64decode(value)
    rsa_key = RSA.importKey(base64.b64decode(private_key))
    cipher = PKCS1_v1_5.new(rsa_key)

    return cipher.decrypt(encrypted_message, '')
