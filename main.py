import random

palavras = ["python", "elefante", "graveto", "computador", "programação", "biscoito", "laranja", "headset", "messi"]

def escolha_palavra():
    return random.choice(palavras)

def jogar_focar(palavra):
    palavra_secreta = palavra
    letras_certas = []
    tentativas = 6

    while True:
        letra = input('Digite uma letra: ').lower()

        if letra in palavra_secreta:
            letras_certas.append(letra)
