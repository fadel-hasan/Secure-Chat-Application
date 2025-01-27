from NoEncryption import NoEncryption
from aes import AESEncryption
from Rsa import RSAEncryption
class EncryptionManager:
    # @staticmethod
    # def get_encryption_strategy(strategy_name, **kwargs):
    #     if strategy_name == 'AES':
    #         return AESEncryption(kwargs['salt'],kwargs['password'])
    #     elif strategy_name == 'RSA':
    #         return RSAEncryption()
    #     else:
    #         raise ValueError("Unknown encryption strategy")
        
        
        
    @staticmethod
    def get_encryption(choice: int):
        if choice == 1:
            with open('key.bin','rb') as r:
                salt = r.read()
            password = input("Enter password for AES encryption: ")
            return AESEncryption(salt,password)
        elif choice == 2:  
            return RSAEncryption()
        elif choice == 3:  
            return NoEncryption()
        else:
            raise ValueError("Invalid encryption choice.")