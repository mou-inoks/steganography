text = "Encrypte moi !"

def text_to_binary(text):
    return ''.join(format(i, '08b') for i in bytearray(text, encoding ='utf-8'))

def binary_to_text(binary_str):
    # Diviser la chaîne binaire en octets de 8 bits
    bytes_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    # Convertir chaque octet binaire en caractère ASCII
    text = ''.join([chr(int(byte, 2)) for byte in bytes_list])
    
    return text

binary_text = text_to_binary(text)

decoded_text = binary_to_text(binary_text)

print(binary_text)
print(decoded_text)

