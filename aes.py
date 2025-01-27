from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from EncryptionStrategy import EncryptionStrategy

class AESEncryption(EncryptionStrategy):


    def __init__(self,salt,password):
        self.key = PBKDF2(password=password,salt=salt,dkLen=32)
        
        
    def generate_keys(self):
        pass  
    
    
    def encrypt_message(self, msg):
        cipher = AES.new(self.key, AES.MODE_CBC)
        iv = cipher.iv
        ciphertext = cipher.encrypt(pad(msg.encode('ascii'),AES.block_size))
        return iv + ciphertext


    def decrypt_message(self, ciphertext):
        iv = ciphertext[:16]
        actual_cipher = ciphertext[16:]
        cipher = AES.new(self.key, AES.MODE_CBC,iv)
        try:
            plaintext =unpad(cipher.decrypt(actual_cipher),AES.block_size)
            return plaintext.decode('ascii')
        except:
            return False

    def get_public_key(self) -> bytes:
        raise NotImplementedError("AES does not use public/private key pairs.")

    def set_public_key(self, public_key: bytes):
        raise NotImplementedError("AES does not use public/private key pairs.")