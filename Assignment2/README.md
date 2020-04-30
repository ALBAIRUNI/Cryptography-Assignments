##This is the solution of cybertalents' genfei challenge, you can access the challenge from [here](https://cybertalents.com/challenges/cryptography/genfei)

##Solution decription:
* The reverse operation of XOR is also XOR, **i.e.**, if **x ^ y = z**, then **y = x ^ z** and **x = y ^ z**
* For each symbol **s**, consider the following:
    * **s** is the original text 
    * **s1** is the text afetr the first step of encryption
    * **s2** is the text after the second step of encryption
* So redefine the encryption steps as follows:
    1. **a1, b1, c1, d1 = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337**
    2. **a2, b2, c2, d2 = c1 ^ F(d1 | F(b1 ^ F(a1)) ^ F(d1 | b1) ^ a1), b1 ^ F(d1 ^ F(a1) ^ (d1 | a1)), a1 ^ F(d1 | F(d1) ^ d1), d1 ^ 1337**
* In the encrypted text, we have **a2, b2, c2, d2** and we want to get **a, b, c, d**
* Decryption steps is done in reverse order of encryption steps, **i.e.**,
  in encryption, from **s** we get **s1** then from **s1** we get **s2**,
  but in decryption, from **s2** we get **s1** then from **s1** we get **s**

* First step of decryption:
    * get **d1** using **d2**
    * get **a1** using **c2, d1**
    * get **b1** using **b2, d1, a1**
    * get **c1** using **a2, d1, a1, b1**
* Second step of decryption:
    * get **a** using **d1**
    * get **d** using **c1, a**
    * get **c** using **b1, a, d**
    * get **b** using **a1, a, d, c** 
* Repeat these two steps **32** times as in encryption