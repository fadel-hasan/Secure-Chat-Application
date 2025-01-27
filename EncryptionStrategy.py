from abc import ABC, abstractmethod

class EncryptionStrategy(ABC):
    @abstractmethod
    def generate_keys(self):
        pass

    @abstractmethod
    def encrypt_message(self, message: str) -> bytes:
        pass

    @abstractmethod
    def decrypt_message(self, encrypted_message: bytes) -> str:
        pass

    @abstractmethod
    def get_public_key(self) -> bytes:
        pass

    @abstractmethod
    def set_public_key(self, public_key: bytes):
        pass
