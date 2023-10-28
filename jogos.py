import forca
import adivinhacao

print("*********************************")
print("*******There we go in the game!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Choose the game? "))

if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()