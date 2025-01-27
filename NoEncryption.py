from EncryptionStrategy import EncryptionStrategy


class NoEncryption(EncryptionStrategy):
    
    def generate_keys(self):
        pass
    
    def encrypt_message(self, message: str) -> bytes:
        return message.encode('utf-8')

    def decrypt_message(self, encrypted_message: bytes) -> str:
        return encrypted_message.decode('utf-8')


    def get_public_key(self):
        return b""

    def set_public_key(self, public_key: bytes):
        pass