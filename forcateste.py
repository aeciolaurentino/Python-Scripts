import random  

def Inicializar():
    apresentação()
    regras_1 = input("Você conhece as regras? Sim/Nao\n").upper()
   
    if regras_1 == 'SIM' or regras_1 == 'S' or regras_1 == 'S': 
        print("Então vamos começar!\n")
        jogar()
    elif regras_1 == 'ou':
        print('Voce se acha muito engraçado\n')
        print('GAME-OVER\n')
    elif regras_1 == 'NAO' or regras_1 == 'NÃO' or regras_1 == 'N':
        print("1° REGRA: Você tem 7 tentativas antes do game-over\n")
        print("2° REGRA: Palavras estão sem acentuação, então não se preocupe\n")
        print("3° REGRA: Se divirta!!!\n")
        return jogar()
    else: 
        print('Não consegui te entender digite apenas: sim ou nao\n')
        return jogar()
def jogar():

    print("Então vamos começar!\n")
    palavra_secreta = carrega_arquivo()
    letras_acertadas = cont_letras_acertadas(palavra_secreta)
       
    enforcou = False
    acertou = False
    qtd = len(palavra_secreta)
    erros = 0

    print("DICAS:")
    print("1°:É uma fruta!")
    print(f'2°:Sua palavra tem {qtd} letras!')

    while(not enforcou and not acertou):
        chute = tentativa()
        if(chute in palavra_secreta):
            cont_acertos(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas        
        print(letras_acertadas)
    if(acertou):
        mensagem_vencedor()
    else:
        mensage_perdedor(palavra_secreta)

def apresentação():
    print('*' * 32)
    print('**\BEM-VINDO AO JOGO DA FORCA/**')
    print('*' * 32)
def carrega_arquivo():

    palavras = []
    with open("frutas.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip().upper()
            palavras.append(linha)
        posicao_do_elemento = random.randrange(0, len(palavras))
        palavra_secreta = palavras[posicao_do_elemento]
        return palavra_secreta
def cont_letras_acertadas(palavra):
    return ["_" for letra in palavra]
def tentativa():
    chute = input('Digite uma letra:')
    chute = chute.strip().upper()
    return chute
def cont_acertos(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute== letra):
            letras_acertadas[index] = letra
        index += 1
def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def mensage_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if(__name__ == "__main__"):
    Inicializar()
