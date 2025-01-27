# Secure Chat Application

This project is a secure chat application that allows users to communicate over a network using different encryption methods. The application supports AES, RSA, and no encryption options, providing flexibility in terms of security and performance.

## Features

- **Server-Client Architecture**: The application is built using a server-client model, where one user hosts the server and others connect as clients.
- **Encryption Options**: Users can choose between AES, RSA, or no encryption for their communication.
- **Key Exchange**: For RSA encryption, the application supports public key exchange between the server and client.
- **Threaded Communication**: Both server and client can send and receive messages simultaneously using threading.

## Prerequisites

- Python 3.x
- `pycryptodome` library for AES encryption
- `rsa` library for RSA encryption

You can install the required libraries using pip:

```bash
pip install pycryptodome rsa
```

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://fadel-hasan/Secure-Chat-Application.git
   cd secure-chat-application
   ```

2. **Generate AES Key**:
   Run the `generate_key.py` script to generate a key for AES encryption:
   ```bash
   python generate_key.py
   ```

3. **Run the Application**:
   - **Server**: Start the server by running:
     ```bash
     python main.py
     ```
     Choose the "Host (Server)" option and follow the prompts.

   - **Client**: Connect to the server by running:
     ```bash
     python main.py
     ```
     Choose the "Connect (Client)" option and follow the prompts.

## Usage

- **Starting the Server**: Enter the host IP and choose an encryption method. The server will wait for a client to connect.
- **Connecting as a Client**: Enter the server IP and the client will connect using the chosen encryption method.
- **Messaging**: Type messages to send them. Type 'close' to end the connection.

## Encryption Methods

- **AES**: Symmetric encryption requiring a password. The password is used to derive a key from a salt stored in `key.bin`.
- **RSA**: Asymmetric encryption using public/private key pairs. Keys are exchanged between server and client.
- **No Encryption**: Messages are sent in plain text.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact

For any questions or issues, please contact [fadl.hasn.work@gmail.com](mailto:fadl.hasn.work@gmail.com).
