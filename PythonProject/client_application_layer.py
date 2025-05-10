import json
import random
from hamming_sed import encode_hamming_16_11
from crypto_utils import encrypt_json_string

BIT_ERROR_RATE = 1

def string_to_bits(s):
    return [int(b) for char in s for b in format(ord(char), '08b')]

def bits_to_blocks(bits, block_size=11):
    padded = bits[:]
    while len(padded) % block_size != 0:
        padded.append(0)
    return [padded[i:i + block_size] for i in range(0, len(padded), block_size)]

def introduce_errors(bits, error_rate):
    noisy_bits = bits[:]
    for i in range(len(noisy_bits)):
        if random.random() < error_rate:
            noisy_bits[i] ^= 1
    return noisy_bits

def prepare_message(op1, op2, operator):
    data = {
        "operand1": op1,
        "operand2": op2,
        "operator": operator,
        "result": "",
        "error": ""
    }

    json_str = json.dumps(data)
    encrypted_bytes = encrypt_json_string(json_str)

    bitstream = [int(b) for byte in encrypted_bytes for b in format(byte, '08b')]

    original_length = len(bitstream)
    length_bits = [int(b) for b in format(original_length, '016b')]
    full_bitstream = length_bits + bitstream

    blocks = bits_to_blocks(full_bitstream)
    codeword_bits = []

    for block in blocks:
        encoded = encode_hamming_16_11(block)
        noisy_encoded = introduce_errors(encoded, BIT_ERROR_RATE)
        codeword_bits.extend(noisy_encoded)

    return codeword_bits

def get_user_input():
    print("Binary Calculator Client")
    print("Enter binary values for operands (only 0s and 1s).")
    try:
        operator = input("Operator (+, -, *, /, &, |, ^): ").strip()
        if operator not in ['+', '-', '*', '/', '&', '|', '^']:
            raise ValueError("Invalid operator.")

        op1 = input("Operand 1: ").strip()
        op2 = input("Operand 2: ").strip()

        if not all(c in '01' for c in op1) or not all(c in '01' for c in op2):
            raise ValueError("Operands must be binary (0 or 1 only).")

        return op1, op2, operator
    except Exception as e:
        print(f"Input error: {e}")
        return None, None, None
