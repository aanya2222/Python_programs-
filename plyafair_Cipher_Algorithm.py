def remove_duplicates(key):
    seen = set()
    result = []
    for char in key:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def generate_matrix(key):
    key = key.replace('j', 'i')
    key = remove_duplicates(key)
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    matrix = [[0] * 5 for _ in range(5)]
    key_index = 0
    alpha_index = 0

    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                matrix[i][j] = key[key_index]
                key_index += 1
            else:
                while alphabet[alpha_index] in key:
                    alpha_index += 1
                matrix[i][j] = alphabet[alpha_index]
                alpha_index += 1

    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt_pair(matrix, pair):
    a, b = pair
    ai, aj = find_position(matrix, a)
    bi, bj = find_position(matrix, b)
    encrypted_pair = ''
    if ai == bi:
        encrypted_pair += matrix[ai][(aj + 1) % 5]
        encrypted_pair += matrix[bi][(bj + 1) % 5]
    elif aj == bj:
        encrypted_pair += matrix[(ai + 1) % 5][aj]
        encrypted_pair += matrix[(bi + 1) % 5][bj]
    else:
        encrypted_pair += matrix[ai][bj]
        encrypted_pair += matrix[bi][aj]
    return encrypted_pair

def playfair_encrypt(plaintext, key):
    matrix = generate_matrix(key)
    plaintext = plaintext.replace('j', 'i').replace(' ', '').lower()
    plaintext_pairs = []
    
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            plaintext_pairs.append(plaintext[i] + 'x')
        else:
            plaintext_pairs.append(plaintext[i] + plaintext[i + 1])
    
    encrypted_text = ''
    for pair in plaintext_pairs:
        encrypted_text += encrypt_pair(matrix, pair)
    
    return encrypted_text

def main():
    plaintext = "instruments"
    key = "monarchy"
    
    encrypted_text = playfair_encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
    main()

