import os
import re

def main():


    while(1):
        os.system('cls')
        print("\n---------- TPC 3 de PL 2023 ----------")
        print("1. Frequência de Processos por Ano.")
        print("2. Frequência de Nomes Próprios.")
        print("3. Frequência de Relação Familiar")
        print("4. Output em Json (gravado tambem em output.json).")

        opt = input("Opção: ")

        try:
            ficheiro = open("processos.txt")
            opt = int(opt)
        except Exception:
            print("Número inválido.")
            exit(-1)

        if opt == 1:
            processaFreqProcessos(ficheiro)
        elif opt == 2:
            primNomes, ultNomes = processaNomesSeculos(ficheiro)
            escreveDict(primNomes, ultNomes)



        ficheiro.close()
        input("\n\n\nPrima qualquer tecla para sair.")

def processaFreqProcessos(ficheiro):
    anos = {}
    for line in ficheiro.readlines():
        x = re.search(r'::(\d\d\d\d)-', line)
        if x != None:
            ano = x.group(1)
            added = 0
            if anos.__contains__(ano):
                anos[ano] += 1
            else:
                anos[ano] = 1
    print(anos)

def processaNomesSeculos(ficheiro):
    primeirosNomes = {}
    ultimosNomes = {}
    for line in ficheiro.readlines():
        data = re.search(r'(\d\d\d\d)-(\d\d)-(\d\d)', line)
        nomesCompleto = re.findall(r"(::[ A-Za-z]+)", line)
        for nome in nomesCompleto:
            nome = nome.replace("::", "").split(" ")
            primeiroNome = nome[0]
            ultimoNome = nome[len(nome)-1]
            if data != None and primeiroNome != "Doc" and primeiroNome != "Em":
                ano = data.group(1)
                seculo = ( int(ano) // 100 ) + 1

                if seculo not in primeirosNomes:
                    primeirosNomes[seculo] = {}
                if seculo not in ultimosNomes:
                    ultimosNomes[seculo] = {}
                if primeiroNome not in primeirosNomes[seculo]:
                    primeirosNomes[seculo][primeiroNome] = 0
                if ultimoNome not in ultimosNomes[seculo]:
                    ultimosNomes[seculo][ultimoNome] = 0
                primeirosNomes[seculo][primeiroNome] += 1
                ultimosNomes[seculo][ultimoNome] += 1
    return (primeirosNomes, ultimosNomes)

def escreveDict(prim, ult):

    primeirosNomes = list(prim.keys())
    primeirosNomes.sort()

    for seculo in primeirosNomes:
        print(f"--- Século {seculo} --- ")

        print("Primeiros nomes: ")
        primNomes = list(prim[seculo].items())
        primNomes.sort(key=lambda x: x[1], reverse=True)

        for i in range(0, 5):
            print(primNomes[i])

        print("Ultimos nomes: ")
        ultNomes = list(ult[seculo].items())
        ultNomes.sort(key=lambda  x: x[1], reverse=True)

        for i in range(0,5):
            print(ultNomes[i])


main()