# === Encodage Hamming 16,11 avec SEC-DED ===
def encode_hamming_16_11(data_bits):
    """Encode 11 bits en un mot de 16 bits (Hamming SEC-DED)."""
    if len(data_bits) != 11:
        raise ValueError("Il faut exactement 11 bits.")

    # Insertion des données aux bonnes positions (hors bits de parité)
    codeword = [0] * 16
    data_positions = [2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14]
    for i, pos in enumerate(data_positions):
        codeword[pos] = data_bits[i]

    # Calcul des bits de parité (P1, P2, P4, P8, parité globale)
    codeword[0] = parity_bit(codeword, [0, 2, 4, 6, 8, 10, 12, 14])    # P1
    codeword[1] = parity_bit(codeword, [1, 2, 5, 6, 9, 10, 13, 14])    # P2
    codeword[3] = parity_bit(codeword, [3, 4, 5, 6, 11, 12, 13, 14])   # P4
    codeword[7] = parity_bit(codeword, [7, 8, 9, 10, 11, 12, 13, 14])  # P8
    codeword[15] = sum(codeword[:15]) % 2                              # parité globale

    return codeword

# === Décodage avec correction 1 bit / détection 2 bits ===
def decode_hamming_16_11(codeword):
    """Décode un mot Hamming 16 bits → 11 bits corrigés (SEC-DED)."""
    if len(codeword) != 16:
        raise ValueError("Il faut 16 bits.")

    # Recalcul des bits de syndrome
    s1 = parity_bit(codeword, [0, 2, 4, 6, 8, 10, 12, 14])
    s2 = parity_bit(codeword, [1, 2, 5, 6, 9, 10, 13, 14])
    s4 = parity_bit(codeword, [3, 4, 5, 6, 11, 12, 13, 14])
    s8 = parity_bit(codeword, [7, 8, 9, 10, 11, 12, 13, 14])
    syndrome = s1 + 2*s2 + 4*s4 + 8*s8

    # Vérification de la parité globale
    overall_parity = sum(codeword[:15]) % 2
    expected_overall = codeword[15]

    if syndrome != 0:
        if overall_parity != expected_overall:
            # Correction d'une erreur 1 bit
            error_pos = syndrome - 1
            if 0 <= error_pos < 16:
                codeword[error_pos] ^= 1
        else:
            # Erreur 2 bits détectée
            raise ValueError("Erreur double détectée, non corrigeable.")

    # Extraction des bits utiles
    data_positions = [2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14]
    return [codeword[pos] for pos in data_positions]

# === Parité paire sur un sous-ensemble d’indices ===
def parity_bit(bits, indices):
    return sum(bits[i] for i in indices) % 2

# === Conversion bits → entier ===
def bits_to_int(bits):
    return int("".join(str(b) for b in bits), 2)

# === Conversion par blocs de 8 bits → texte ===
def bits_to_string(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        chars.append(chr(int("".join(str(b) for b in byte), 2)))
    return ''.join(chars)
