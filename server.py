import socket
import threading
import os
from EncryptionManager import EncryptionManager as em
class Server:
    
    
    def __init__(self,HOST,encryption_type,PORT=9999):
        self.name = input("Enter your name: ")
        # self.encryption = encryption_strategy
        self.encryption = em.get_encryption(choice=encryption_type)
        
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        self.bind_and_listen(HOST, PORT)
        
        
        self.client_socket, address = self.socket.accept()
        
        self.client_socket.send(str(encryption_type).encode('utf-8')) 

        if encryption_type ==2:
            self.exchange_keys()
        
        print('connection from : ' + str(address))
        
        self.talk_to_client()
        
        
        
    def bind_and_listen(self, host, port):
        try:
            self.socket.bind((host, port))
            self.socket.listen()
            print("Server waiting for connection...")
        except socket.error as e:
            print(f"Socket error: {e}")
            os._exit(1)
            
            
    def exchange_keys(self):
        # Send server's public key to the client
        self.client_socket.send(self.encryption.get_public_key())

        # Receive client's public key
        client_public_key = self.client_socket.recv(1024)
        self.encryption.set_public_key(client_public_key)
        print("Exchanged public keys with the client.")
        
        
    def talk_to_client(self):
        self.keep_running = True 
        threading.Thread(target = self.receive_message).start()
        self.send_message()
        
        
   
    def send_message(self):
        while self.keep_running:  
            try:
                server_message = input('')
                if server_message.strip().lower() == 'close':
                    self.client_socket.send(self.encryption.encrypt_message('close'))
                    self.close_connection()
                    break
                message_with_name = f"{self.name}: {server_message}"
                encrypted_message = self.encryption.encrypt_message(message_with_name) 
                self.client_socket.send(encrypted_message)
            except OSError:
                print("Cannot send message, client socket is closed.")
                break       
            
   
    def receive_message(self):
        while self.keep_running:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    print("Connection disconnected.")
                    self.close_connection()
                    break
                
                client_message = self.encryption.decrypt_message(data)

                if client_message.strip().lower() == 'close':
                    print("Client requested to close the connection.")
                    self.close_connection()
                    break
                print("\033[1;31;40m" + client_message + '\033[0m')
            except ConnectionResetError:
                print("Connection was forcibly closed by the client.")
                self.close_connection()
                break
            except Exception as e:
                print(e)
                self.close_connection()
                break
    
    def close_connection(self):
        self.keep_running = False
        self.client_socket.close()
        self.socket.close()
        os._exit(0)
            
            
# Server('127.0.0.1',7632)