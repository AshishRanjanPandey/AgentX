def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def add_sentinel(text):
    return text + "$$$"
