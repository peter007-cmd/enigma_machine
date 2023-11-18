from plugboard import Plugboard
from reflector import Reflect
from rotors import Rotor
from keyboard import KeyBoard
from enigma import Enigma

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")

k = KeyBoard()
p = Plugboard(["AB", "CD", "EF"])
e = Enigma(B,IV,II,I,p,k)
e.set_rings((5,26,2))
e.set_key("CAT")

message = "THISCOOLENIGMAMACHINE"
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + e.encipher(letter)
print(cipher_text)
