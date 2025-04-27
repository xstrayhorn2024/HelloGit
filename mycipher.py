import sys

def caesar_cipher(text, shift):
    result = ''
    for char in text.upper():
        if char.isalpha():
            shifted = ord(char) + shift
            if shifted > ord('Z'):
                shifted -= 26
            result += chr(shifted)
    return result

def group_output(text):
    blocks = [text[i:i+5] for i in range(0, len(text), 5)]
    lines = [blocks[i:i+10] for i in range(0, len(blocks), 10)]
    for line in lines:
        print(' '.join(line))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 mycipher.py <shift>")
        sys.exit(1)

    shift = int(sys.argv[1]) % 26
    input_text = ''.join(sys.stdin.readlines())
    encoded = caesar_cipher(input_text, shift)
    group_output(encoded)

