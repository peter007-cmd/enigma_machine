from plugboard import Plugboard
from reflector import Reflect
from rotors import Rotor
from keyboard import KeyBoard
from enigma import Enigma
from draw import draw
import pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")
MONO = pygame.font.SysFont("FreeMono",25)
BOLD = pygame.font.SysFont("FreeMono",25,bold=True)

WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
MARGINS = {"top":200,"bottom":200,"left":100,"right":100}
INPUT = ""
OUTPUT = ""
GAP = 100
PATH = []
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
e.set_rings((1,1,1))
e.set_key("CAT")
"""
message = "THISCOOLENIGMAMACHINE"
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + e.encipher(letter)
print(cipher_text)
"""
animating = True
while animating:
    SCREEN.fill("#333333")
    text = BOLD.render(INPUT,True,"white")
    text_box = text.get_rect(center=(WIDTH/2,MARGINS['top']/3))
    SCREEN.blit(text,text_box)
    draw(e,PATH,SCREEN,WIDTH,HEIGHT,MARGINS,GAP,BOLD)

    text = MONO.render(OUTPUT,True,"white")
    text_box = text.get_rect(center=(WIDTH/2,MARGINS['top']/3+25))
    SCREEN.blit(text,text_box)
    draw(e,PATH,SCREEN,WIDTH,HEIGHT,MARGINS,GAP,BOLD)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            animating = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                IV.rotate()
            elif event.key==pygame.K_SPACE:
                INPUT+=" "
                OUTPUT+=" "
            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT+letter
                    PATH,cipher = e.encipher(letter)
                    OUTPUT = OUTPUT+cipher
