Requirements
Python 3.8 or above
PyQt5
pycryptodome (for AES encryption)
Network access (TCP/IP)

Setup Instructions
1. Install Python and Dependencies
Ensure that you have Python 3.8 or above installed. Then, install the required Python libraries by running the following command in your terminal or command prompt:
pip install PyQt5 pycryptodome

2. Running the Client (Automatically Starts Server)
To run both the client and the server, open a terminal (or command prompt), navigate to the folder where the code is located, and run the main.py script:
python main.py
This will start the server in a separate thread (automatically) and launch the calculator GUI. You can enter arithmetic operations and click Calculer to get the result. The client will send the request to the server, which processes it and sends back the result.

3. Running Server and Client Separately
While the client will automatically run the server in the same process, you can also run the server and the client separately if desired:
Server: Open a terminal and run the server script:
python server_transport_layer.py
Client: In another terminal, run the (client_transport_layer.py
 script.
The server will print logs in the terminal window, showing incoming requests from the client.