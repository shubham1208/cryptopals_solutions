import string
import re

in_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def take(n, s):
    for y in range(0, n, 2):
            yield s[i:i+2]

def hex2str(s):
    return bytes.fromhex(s).decode("ascii")

def string_xor(s, c):
    c = ord(c)  # dirty dynamic typing
    return ''.join(map(lambda h: chr(ord(h) ^ c), s))

for letter in string.ascii_letters:
    result = string_xor(hex2str(in_hex), letter)
    # remove ascii control chars
    pretty_result = re.sub(r'[\x00-\x1F]+', '', result)
    # print the result and the corresponding letter used to decode
    print(f'{letter}: {pretty_result}')
