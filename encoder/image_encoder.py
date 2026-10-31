import os
from PIL import Image
from encoder.binary_utils import text_to_binary, add_sentinel


def encode_message(image_path, message, output_path="output/secret.png"):
    # ---------- SAFETY CHECKS ----------
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Cover image not found: {image_path}")

    if not message.strip():
        raise ValueError("Secret message is empty")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # ---------- OPEN IMAGE ----------
    image = Image.open(image_path).convert("RGBA")
    pixels = list(image.getdata())

    # ---------- PREPARE MESSAGE ----------
    message = add_sentinel(message)
    binary = text_to_binary(message)

    # ---------- CAPACITY CHECK ----------
    max_bits = len(pixels) * 3
    if len(binary) > max_bits:
        raise ValueError("Message too large for this image")

    data_index = 0
    new_pixels = []

    # ---------- ENCODE ----------
    for r, g, b, a in pixels:
        if data_index < len(binary):
            r = (r & ~1) | int(binary[data_index])
            data_index += 1

        if data_index < len(binary):
            g = (g & ~1) | int(binary[data_index])
            data_index += 1

        if data_index < len(binary):
            b = (b & ~1) | int(binary[data_index])
            data_index += 1

        new_pixels.append((r, g, b, a))

    # ---------- SAVE ----------
    image.putdata(new_pixels)
    image.save(output_path, "PNG")

    print(f"✅ AGENTX: Encoded image saved → {output_path}")
    return output_path
