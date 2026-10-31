from PIL import Image

def decode_message(image_path):
    image = Image.open(image_path).convert("RGBA")
    pixels = list(image.getdata())

    binary = ""
    for pixel in pixels:
        for color in pixel[:3]:
            binary += str(color & 1)

    message = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        char = chr(int(byte, 2))
        message += char
        if "$$$" in message:
            return message.replace("$$$", "")

    return ""
