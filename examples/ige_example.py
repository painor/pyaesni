import pyaesni

data = b'A' * 16
key = b'B' * 32
iv = b'C' * 32

result = pyaesni.ige256_encrypt(data, key, iv)
if result == b'\x8bb\xcf\n\xb9aD\xde\xa9c\xfe9\x91\xf8\xd0B':
    print("encryption is working fine")
else:
    print("encryption broken! please check installation again")
    exit(0)

decrypted = pyaesni.ige256_decrypt(result, key, iv)
if decrypted == data:
    print("decryption is working fine")
else:
    print("decryption broken! please check installation again")
    exit(0)

print("All good!")
