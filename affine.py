def modular_inverse(a, m):
    for x in range(m):
        if(a * x) % m == 1:
            return x
    return None

def decrypt_affine(ciphertext, a, b, m=26):
    a_inv = modular_inverse(a, m)
    if a_inv is None:
        raise ValueError("no")

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y-b)) % m 
            plaintext += chr(x+ord('A'))
        else:
            plaintext += char
    return plaintext
ciphertext = "ZVSXRKPIUNT"
a, b = 9, 24
print(decrypt_affine(ciphertext, a, b))
