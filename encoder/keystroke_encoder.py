# encoder/keystroke_encoder.py

import time
import os


def encode_keystroke(message: str, output_file="output/keystroke_encoded.txt"):
    """
    Encodes a message as simulated keystroke timing data.
    Each character is mapped to a delay pattern.
    """

    if not message:
        raise ValueError("Message cannot be empty")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    timings = []
    base_delay = 0.08  # seconds

    for char in message:
        delay = base_delay + (ord(char) % 10) * 0.01
        timings.append(f"{char}:{round(delay, 3)}")

        # simulate typing delay (non-blocking for realism)
        time.sleep(0.005)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(timings))

    return output_file
