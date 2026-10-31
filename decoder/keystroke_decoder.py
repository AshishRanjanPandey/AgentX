# decoder/keystroke_decoder.py

import os


def decode_keystroke(file_path="output/keystroke_encoded.txt"):
    """
    Decodes a keystroke timing encoded message.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError("Keystroke encoded file not found")

    message = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                char, _ = line.split(":", 1)
                message.append(char)

    if not message:
        raise ValueError("No valid keystroke data found")

    return "".join(message)
