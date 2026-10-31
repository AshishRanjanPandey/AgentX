import time
import os

def encode_clock(message: str, output_file="output/clock_encoded.txt"):
    if not message:
        raise ValueError("Message cannot be empty")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Convert message to binary (8 bits per char)
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    timestamps = []

    for bit in binary_message:
        # Record the start of the bit
        timestamps.append(str(time.time()))

        # Sleep to create the "Gap" (The Technique)
        if bit == '0':
            time.sleep(0.05)
        else:
            time.sleep(0.15)
            
    # 🔥 CRITICAL FIX: Add the final timestamp to close the last bit
    timestamps.append(str(time.time()))

    # Save to file
    with open(output_file, "w") as f:
        f.write("\n".join(timestamps))

    return output_file
