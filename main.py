from server import Server
from client import Client
def main():
    
    
    print("Select mode:")
    print("1. Host (Server)")
    print("2. Connect (Client)")
    
    try:
        choice = int(input("Enter your choice (1/2): "))
        if choice == 1:
            start_server()
        elif choice == 2:
            connect_to_server()
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number.")
        
def start_server():
    host = input("Enter the host IP: ")
    encryption_choice = get_encryption_choice()
    Server(host, encryption_choice)
    
def connect_to_server():
    host = input("Enter the server IP: ")
    Client(host)
    
    
def get_encryption_choice():
    while True:
        try:
            choice = int(input("Choose encryption type:\n1) AES\n2) RSA\n3) No encryption\n"))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice, please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")
            
if __name__ == "__main__":
    main()