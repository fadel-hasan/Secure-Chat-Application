import socket
import threading
import os
from EncryptionManager import EncryptionManager as em

class Client:
    
    def __init__(self, HOST,PORT=9999):
        self.name = input("Enter your name: ")
        self.socket = socket.socket()
       
        
        self.connect_to_server(HOST, PORT)
        
        self.encryption_choice = int(self.socket.recv(1024).decode('utf-8'))
        
        print('enc: ',self.encryption_choice)
        
        self.encryption = em.get_encryption(choice=self.encryption_choice)
        
        if self.encryption_choice == 2:
            self.exchange_keys()            
        
        print("Connected to the server.")
        
        self.talk_to_server()
        
        
        
    def connect_to_server(self, host, port):
        try:
            self.socket.connect((host, port))
        except socket.error as e:
            print(f"Connection error: {e}")
            os._exit(1)
            
    def talk_to_server(self):
        self.keep_running = True
        threading.Thread(target=self.receive_message).start()
        self.send_message()
        
        
            
            
    def exchange_keys(self):
        # Receive server's public key
        server_public_key = self.socket.recv(1024)
        self.encryption.set_public_key(server_public_key)

        # Send client's public key to the server
        self.socket.send(self.encryption.get_public_key())
        print("Exchanged public keys with the server.")
    
            
    def send_message(self):
        while self.keep_running:
            client_message = input('')
            if client_message.strip().lower() == 'close':
                self.socket.send(self.encryption.encrypt_message('close'))
                self.close_connection()
                break
            message_with_name = f"{self.name}: {client_message}"
            encrypted_message = self.encryption.encrypt_message(message_with_name)
            self.socket.send(encrypted_message)
            
        
    
    def receive_message(self):
        while self.keep_running:
            try:
                data = self.socket.recv(1024)
                if not data:
                    print("Connection disconnected.")
                    self.close_connection()
                    break
               
                server_message = self.encryption.decrypt_message(data)
                if not server_message and self.encryption_choice == 1:
                    print('you enter a valid password try later')
                    self.close_connection()
                    break
                if server_message.strip().lower() == 'close':
                    print("Server requested to close the connection.")
                    self.close_connection()
                    break
                print("\033[1;32;40m" + server_message + '\033[0m')
            except ConnectionResetError:
                print("Connection was forcibly closed by the server.")
                self.close_connection()
                break
    
    def close_connection(self):
        self.keep_running = False
        self.socket.close()
        os._exit(0)