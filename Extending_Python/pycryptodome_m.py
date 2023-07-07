from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA

# AES Encryption and Decryption
key = get_random_bytes(16)  # 16 bytes (128 bits) key for AES-128
cipher = AES.new(key, AES.MODE_ECB)
plaintext = b'This is a secret message.'
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
print("AES Encryption: ", ciphertext)
print("AES Decryption: ", decrypted_text)

# Hashing (SHA-256)
data = b'This is a data to be hashed.'
hash_object = SHA256.new(data)
hashed_data = hash_object.digest()
print("Hashed data: ", hashed_data)

# Digital Signature (RSA)
private_key = RSA.generate(2048)
public_key = private_key.publickey()

message = b'This is a message to be signed.'
signature = pkcs1_15.new(private_key).sign(message)
verified = False
try:
    pkcs1_15.new(public_key).verify(message, signature)
    verified = True
except (ValueError, TypeError):
    verified = False

print("Signature Verification: ", verified)