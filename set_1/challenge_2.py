a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"

def sxor(s1,s2):    
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def xor(str1, str2):
    decoded_str1 = bytes.fromhex(str1).decode('utf-8')
    print("dc1: ",decoded_str1)
    decoded_str2 = bytes.fromhex(str2).decode('utf-8')
    print("dc2: ",decoded_str2)
    x = sxor(decoded_str1, decoded_str2)

    return(x)

print(xor(a,b).encode("utf-8").hex())