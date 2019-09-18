# AES 256 encryption/decryption using pycrypto library
import base64
import hashlib

from Crypto.Cipher import AES

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(
    BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt_option(raw, question_id):
    """
    Encrypt user answer's option as this message is send to client
    """
    private_key = hashlib.sha256(
        bytearray('dSk9Degs09b', "utf-8")).digest()
    zero_byte_padding = BLOCK_SIZE - len(question_id)

    iv = question_id + zero_byte_padding * '\x00'
    iv = iv.encode('utf-8')
    cleartext = bytearray(pad(raw), 'utf-8')
    cipher = AES.new(private_key, AES.MODE_CBC, iv)

    return base64.b64encode(cipher.encrypt(bytes(cleartext)))


if __name__ == '__main__':
    # First let us encrypt secret message
    encrypted = encrypt_option("0", '11869021011')
    print("encrypted: ", encrypted)
    #
    encrypted = encrypt_option("1", '11869021012')
    print("encrypted: ", encrypted)

    encrypted = encrypt_option("2", '11869021015')
    print("encrypted: ", encrypted)
    #
    # encrypted:  b'+I5Blrvn/LjEQyByOP8cmA=='
    # encrypted:  b'vzHQG2g61z0oEO4kbqU9pQ=='
    # encrypted:  b'eqrzkr3CzXfH15t/dUxiyQ=='

    import hashlib
    m = hashlib.md5()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    print(m)
    res = m.digest()
    print(res)
    # b'\\xbbd\\x9c\\x83\\xdd\\x1e\\xa5\\xc9\\xd9\\xde\\xc9\\xa1\\x8d\\xf0\\xff\\xe9'

# More
# condensed:

    res2 = hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest()
    print(res2)
    # 'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'
