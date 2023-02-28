import os

def main():
    opcao = 0

    while (opcao != 9):
        os.system('cls')
        print("\n---------- TPC 2 de PL 2023 ----------")
        print("1: Ler ficheiro.")
        print("2: Ler input do teclado.")
        print("9: Sair ")
        opcao = input("Opção: ")
        somaAt = 0
        try:
            opcao = int(opcao)
        except ValueError:
            print("Por favor introduza um número!")

        if opcao == 1:
            nomeFicheiro = input("Caminho para o ficheiro: ")

            try:
                ficheiro = open(nomeFicheiro)

                parse(ficheiro.readlines())
                input("")
            except Exception:        
                print("Ficheiro não encontrado")
                input("Prima uma tecla para continuar...." + e.getMessage())

        elif opcao == 2:
            print("Começe a digitar: ")
            parse()
        elif opcao == 9:
            break;


def parse(ficheiro = 0):
    if ficheiro != 0:
        digitos, off = 0,0
        for line in ficheiro:
            texto = line.upper()
            for elemento in range(0, len(texto)):
                char = texto[elemento]
                if char == 'O':
                    if texto[elemento:elemento+3] == "OFF":
                        off = 1
                    if texto[elemento:elemento+2] == "ON":
                        off = 0
                if char == "=":
                    print(digitos)
                if off == 0:
                    if 48 <= ord(char) <= 57:
                        digitos += 1
    else:
        texto = ""
        digitos, off = 0,0
        while True:
            textoAtual = input()
            textoAtual = textoAtual.upper()

            texto += textoAtual
            for elemento in range(0, len(textoAtual)):
                char = textoAtual[elemento]
                if char == 'O':
                    if textoAtual[elemento:elemento+3] == "OFF":
                        off = 1
                    if textoAtual[elemento:elemento+2] == "ON":
                        off = 0
                if char == "=":
                    print(digitos)
                if off == 0:
                    if 48 <= ord(char) <= 57:
                        digitos += 1



main()