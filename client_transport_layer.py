import socket
import logging
from client_application_layer import prepare_message, get_user_input

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

HOST = 'localhost'
PORT = 5000

def run_client():
    logging.info("Client starting...")

    while True:
        op1, op2, operator = get_user_input()
        if op1 is None:
            logging.warning("Invalid input. Please try again.")
            continue
        break

    bitstream = prepare_message(op1, op2, operator)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logging.info(f"Connecting to server at {HOST}:{PORT}")
            s.connect((HOST, PORT))

            bit_string = ''.join(str(bit) for bit in bitstream)
            logging.info("Sending bitstream to server...")
            s.sendall(bit_string.encode())

            response = s.recv(4096).decode()
            logging.info("Received response from server.")

            print("\n--- Server Response ---")
            print(response)

    except ConnectionRefusedError:
        logging.error("Failed to connect to server. Is it running?")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    run_client()
