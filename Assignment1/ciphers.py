import sys


class Shift:

    def encrypt(self, plain, a):
        cipher = ''
        for ch in plain:
            i = char_to_int(ch)
            i = (i + a) % 26
            ch = int_to_char(i)
            cipher += ch
        return cipher

    def decrypt(self, cipher, a):
        plain = ''
        for ch in cipher:
            i = char_to_int(ch)
            i = (i - a + 26) % 26
            ch = int_to_char(i)
            plain += ch
        return plain

class Affine:

    def encrypt(self, plain, a, b):
        cipher = ''
        for ch in plain:
            i = char_to_int(ch)
            i = (a * i + b) % 26
            ch = int_to_char(i)
            cipher += ch
        return  cipher

    def decrypt(self, cipher, a, b):
        plain = ''
        for ch in cipher:
            i = char_to_int(ch)
            if mul_inverse(a, 26) == -1:
                return 'Can\'t decrypt the message, {} and 26 are coprimes'.format(a)
            i = ((i - b + 26) * mul_inverse(a, 26)) % 26
            ch = int_to_char(i)
            plain += ch
        return plain

class Vigenere:

    def generate_full_key(self, text, key):
        full_key = ''
        idx = 0
        while len(full_key) < len(text):
            full_key += key[idx]
            idx = (idx + 1) % len(key)
        return full_key

    def encrypt(self, plain, key):
        key = self.generate_full_key(plain, key)
        cipher = ''
        for idx in range(len(key)):
            i = (char_to_int(plain[idx]) + char_to_int(key[idx])) % 26
            ch = int_to_char(i)
            cipher += ch
        return  cipher

    def decrypt(self, cipher, key):
        key = self.generate_full_key(cipher, key)
        plain = ''
        for idx in range(len(key)):
            i = (char_to_int(cipher[idx]) - char_to_int(key[idx]) + 26) % 26
            ch = int_to_char(i)
            plain += ch
        return  plain

def char_to_int(ch):
    return ord(ch) - ord('A')

def int_to_char(i):
    return chr(i + ord('A'))

def mul_inverse(x, mod):
    for i in range(mod):
        if (x * i) % mod == 1:
            return i
    return -1

if __name__ == '__main__':
    args = sys.argv
    algorithm, operation, in_file, out_file = args[1:5]
    in_file = open(in_file, 'r')
    text = in_file.read()
    in_file.close()
    ans = None

    if algorithm == 'shift':
        shift = Shift()
        a = int(args[-1])
        if operation[0] == 'e':
            ans = shift.encrypt(text, a)
        else:
            ans = shift.decrypt(text, a)
    elif algorithm == 'affine':
        affine = Affine()
        a, b = int(args[-2]), int(args[-1])
        if(operation[0] == 'e'):
            ans = affine.encrypt(text, a, b)
        else:
            ans = affine.decrypt(text, a, b)
    elif algorithm == 'vigenere':
        vigenere = Vigenere()
        key = args[-1]
        if(operation[0] == 'e'):
            ans = vigenere.encrypt(text, key)
        else:
            ans = vigenere.decrypt(text, key)

    out_file = open(out_file, 'w')
    out_file.write(str(ans))
    out_file.close()
