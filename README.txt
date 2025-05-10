# Binary Calculator: Client-Server System with Error Correction and Encryption

This project is a Python-based binary calculator that uses a client-server architecture to simulate secure and reliable communication. It integrates:

- Hamming (16,11) error correction code  
- AES encryption for data confidentiality  
- TCP sockets for communication  
- A PyQt5 GUI for user interaction

This application is designed as a practical demonstration of secure data transmission over unreliable networks.

## Features

- Graphical interface for binary operations  
- AES encryption of messages  
- Error correction using Hamming code  
- Client-server architecture via TCP sockets  
- Simulated noisy channel for testing  

## Requirements

- Python 3.8 or higher  
- PyQt5  
- pycryptodome  

Project Structure:
/project-folder
│
├── main.py                     # Launches GUI and starts the server thread
├── ui_calculator.py            # PyQt5 interface generated with Qt Designer
├── client_application_layer.py # Prepares encrypted, encoded messages
├── client_transport_layer.py   # Sends messages to the server via TCP
├── server_application_layer.py # Decodes, decrypts, and processes the request
├── server_transport_layer.py   # Receives and replies to client messages
├── hamming_sed.py              # Hamming (16,11) encoding and decoding
├── crypto_utils.py             # AES CBC encryption/decryption helpers

How to Run
Option 1: Run client and server together (default)
Launch the GUI (the server starts automatically in a background thread):
python main.py

Option 2: Run client and server separately
In separate terminals:
# Terminal 1 (Server)
python server_transport_layer.py

# Terminal 2 (Client)
python client_transport_layer.py

Network Configuration (Optional)
To run the system across two devices:

Connect both to the same Wi-Fi or hotspot.

On the server device, run ipconfig (Windows) or ifconfig (Linux/Mac) to get the IP address.

Replace 'localhost' in the client code with that IP.

Make sure your firewall allows Python to receive TCP connections on port 5000.

Security and Reliability Details
AES (CBC Mode): Protects data in transit using symmetric encryption

Hamming (16,11): Corrects single-bit errors, detects two-bit errors

Bit Error Simulation: Errors are introduced to test the reliability of error correction

Limitations and Possible Improvements
Only one client can connect at a time (no multithreading on the server)

Hardcoded AES key; RSA-based key exchange was attempted but not implemented

The project is local or LAN-based; cloud deployment is a future possibility

Authors
Mahmoud Nour

Bouslahi Yosr

Project supervised by Mr. Karoui Kamel.
Created as part of an academic assignment.
