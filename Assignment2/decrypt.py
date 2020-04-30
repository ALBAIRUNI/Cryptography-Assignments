
import sys
from struct import pack, unpack

def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32

def decrypt(block):
    a, b, c, d = unpack("<4I", block)
    for rno in xrange(32):
        tmp_a = a
        d = d ^ 1337
        a = c ^ F(d | F(d) ^ d)
        b = b ^ F(d ^ F(a) ^ (d | a))
        c = tmp_a ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a)

        tmp_a = a
        a = d ^ 31337
        d = c ^ F(a | F(a) ^ a)
        c = b ^ F(a ^ F(d) ^ (a | d))
        b = tmp_a ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)
    return pack("<4I", a, b, c, d)

pt = open(sys.argv[1]).read()

ct = "".join(decrypt(pt[i:i+16]) for i in xrange(0, len(pt), 16))
i = -1
while ct[i] == '#': i -= 1
ct = ct[:i+1]
open(sys.argv[1][:-4], "w").write(ct)