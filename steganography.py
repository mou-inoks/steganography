from PIL import Image

current_image = "C:\\Users\\Salim\\Downloads\\chien.png"


def decode(image):

    image = Image.open(current_image)

    width, height = image.size

    extracted_bits = ''

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))

            for i in range(3):
                extracted_bits += str(pixel[i] & 1)

    extracted_text = ''
    for i in range(0, len(extracted_bits), 8):
        byte = extracted_bits[i:i + 8]
        extracted_text += chr(int(byte, 2))

    end_index = extracted_text.find('\x00')

    if end_index != -1:
        extracted_text = extracted_text[:end_index]

    print("image texte décodé:", extracted_text)


def code(current_image):

    text_to_encode = "My encoded text"
    
    text_to_binary = ''.join(format(ord(char), '08b') for char in text_to_encode)
    
    image = Image.open(current_image)

    width, height = image.size

    text_index = 0

    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))

            for i in range(3):
                if text_index < len(text_to_binary):
                    pixel[i] = (pixel[i] & 0b11111110) | int(text_to_binary[text_index])
                    text_index += 1
                else:
                    break

            image.putpixel((x, y), tuple(pixel))

    image.save("encoded.png")
    
    print("Encodé avec succès ")
    


encoded_image = "C:\\Users\\Salim\\Desktop\\Encode\\encoded.png"
# code(current_image)
decode(encoded_image)