import random

palavras = ["python", "professor", "messi", "programação", "headset", "queijo", "laranja", "televisão", "elefante"]

def escolha_palavra():
    return random.choice(palavras)

def jogar_focar(palavra):
    palavras_secreta = palavra
    letras_certa = []
    tentativas = 6


    while True:
        letra = input('Digite uma letra: ').lower()

        if letra in palavras_secreta:
            letras_certa.append(letra)
        else:
            tentativas -=1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes ")

        palavra_exibidia = " "
        for letra_secreta in palavras_secreta:
            if letra_secreta in letras_certa:
                palavra_exibidia += letra_secreta + " "

            else:
                palavra_exibidia += "_ "

        print(palavra_exibidia)

        if palavra_exibidia.replace(" ", "") == palavras_secreta:
            print("Parabéns, você acertou a palavra!")
            break

        if tentativas == 0:
            print(f"Fim de jogo! A palavra era '{palavras_secreta}'.")



print("Bem-vindo ao Jogo da Forca!")
palavra_escolhida = escolha_palavra()
jogar_focar(palavra_escolhida)