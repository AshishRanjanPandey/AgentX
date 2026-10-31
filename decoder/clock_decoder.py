def decode_clock(file_path="output/clock_encoded.txt"):
    """
    Decodes message from time-gap covert channel.
    0 bit -> delay around 0.5 sec
    1 bit -> delay around 1.5 sec
    """

    try:
        with open(file_path, "r") as f:
            timestamps = [float(line.strip()) for line in f if line.strip()]

        if len(timestamps) < 2:
            return "❌ Not enough data to decode"

        binary_bits = []

        # Calculate time differences
        for i in range(1, len(timestamps)):
            diff = timestamps[i] - timestamps[i - 1]

            # Threshold detection
            if diff < 0.1:
                binary_bits.append('0')
            else:
                binary_bits.append('1')

        # Join bits
        binary_string = ''.join(binary_bits)

        # Convert binary to text (8 bits per character)
        message = []
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            if len(byte) == 8:
                message.append(chr(int(byte, 2)))

        return ''.join(message)

    except Exception:
        return "❌ Clock encoded file missing or corrupted"
