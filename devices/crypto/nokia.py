#
# Implements a custom AES256 based password encryption scheme
#
# Note: router must be configured accordingly:
# /admin system security hash-control custom-hash algorithm aes256 key "09123456789012345678901234567890"
#
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# KEY = hashlib.sha256(passphrase).digest()# returns 256 bit key
KEY = "09123456789012345678901234567890".encode('ascii') # 32-character magic key, must match router

#
# Returns an AES256-encrypted 32-char string
# Note: 'salt' is ignored
#
def encrypt(value, salt=None):
  if not value:
    return ""
  cipher = AES.new(KEY,AES.MODE_ECB) #creates a AES-256 instance using ECB mode
  ciphertext = base64.b64encode(cipher.encrypt(pad(value.encode('utf-8'),16)))
  return ciphertext.decode('ascii')

#
# Reverse the hashing process
#
def decrypt(value):
  if not value:
    return ""
  cipher = AES.new(KEY,AES.MODE_ECB) #creates a AES-256 instance using ECB mode
  return unpad(cipher.decrypt(base64.b64decode(value)),16).decode('utf-8')

if __name__ == "__main__":
    PASSWORD = "HELLO"
    encrypted = encrypt(PASSWORD)
    print( encrypted )
    decrypted = decrypt(encrypted)
    print( f"{decrypted} == {PASSWORD}" )
