from matplotlib import pyplot as plt
import os
from prettytable import PrettyTable


def main():
    listaUtentes = parser("myheart.csv")
    #print(listaUtentes)
    opcao = 0

    while (opcao != 9):
        os.system('cls')
        print("\n---------- TPC 1 de PL 2023 ----------")
        print("1: Distribuição da doença por sexo.")
        print("2: Distribuição da doença por escalão etária.")
        print("3: Distribuição da doença por níveis de colestrol.")
        print("9: Sair ")
        opcao = input("Opção: ")
        try:
            opcao = int(opcao)
        except ValueError:
            print("Por favor introduza um número!")

        print("Resultado de: ")
        if opcao == 1:
            print("Distribuição da doença por sexo")
            dist = doencaPorSexo(listaUtentes)
            desenhaTabelasSexo(dist)

            imprimir = input("Imprimir gráfico ? (Y/N)")

            if imprimir == "Y":
                count = list(dist.values())
                plt.bar(range(len(dist)), count, width=0.5, align='center')
                plt.xticks(range(len(dist)), ["M", "F"], fontsize=10)
                plt.yticks(fontsize=7)
                plt.xlabel("Sexo")
                plt.ylabel("Nº de doentes")
                plt.show()
        elif opcao == 2:
            print("Distribuição da doença por escalão etária")
            resp = escaloesEtarios(listaUtentes)
            desenhaTabelaEscEt(resp)

            grafico = input("Imprimir gráfico ? (Y/N)")
            if grafico == "Y":
                count = list(resp.values())
                plt.bar(range(len(resp)), count, width=0.5, align='center')
                plt.xticks(range(len(resp)), [f"[{inf},{sup}]" for inf, sup in resp.keys()], fontsize=6)
                plt.yticks(fontsize=7)
                plt.xlabel("Intervalos Etários")
                plt.ylabel("Nº de doentes")
                plt.show()
        elif opcao == 3:
            print("Distribuição da doença por níveis de colestrol")
            resp = doecaPorNiveisColestrol(listaUtentes)
            desenhaTableasColestrol(resp)

            grafico = input("Imprimir gráfico ? (Y/N)")
            if grafico == "Y":
                count = list(resp.values())
                plt.bar(range(len(resp)), count, width=0.5, align='center')
                plt.xticks(range(len(resp)), [f"[{inf},{sup}]" for inf, sup in resp.keys()], fontsize=6)
                plt.yticks(fontsize=7)
                plt.xlabel("Intervalos de Colestrol")
                plt.ylabel("Nº de doentes")
                plt.show()
        elif opcao == 9:
            break;

def parser(path):
    listaUtentes = {}  # dicionário que vai ter como keys o nome da propriedade e value um dicionário com keys um id que é um acumulador e value o valor da propriedade
    linha = 2
    id = 0
    idade = {}
    sexo = {}
    tensao = {}
    colestrol = {}
    batimento = {}
    temDoenca = {}

    with open(path, 'r') as file:
        next(file)

        for line in file:
            colunas = line.strip().split(',')
            if len(colunas) != 6: return print(f"Fatam elementos na linha {linha}")
            else:
                idade[id] = colunas[0]
                sexo[id] = colunas[1]
                tensao[id] = colunas[2]
                colestrol[id] = colunas[3]
                batimento[id] = colunas[4]
                temDoenca[id] = colunas[5]
                id += 1
                linha += 1

    listaUtentes["IDADE"] = idade
    listaUtentes["SEXO"] = sexo
    listaUtentes["TENSAO"] = tensao
    listaUtentes["COLESTROL"] = colestrol
    listaUtentes["BATIMENTO"] = batimento
    listaUtentes["TEMDOENCA"] = temDoenca

    return listaUtentes

def doencaPorSexo(listaUtentes):
    dist = {"Masculino" : 0,
            "Feminino" : 0}

    for id,valor in listaUtentes["SEXO"].items():
        if listaUtentes["TEMDOENCA"][id] == "1":
            if valor == "M":
                dist["Masculino"] += 1
            elif valor == "F":
                dist["Feminino"] += 1
    return dist

def escaloesEtarios(listaUtentes):
    dist = {}
    for i in range(30, 90, 5):
        dist[(i, i+4)] = 0

    for id,valor in listaUtentes["IDADE"].items():
        if listaUtentes["TEMDOENCA"][id] == "1":
            for inf,sup in dist:
                if inf <= int(valor) <= sup:
                    dist[(inf,sup)] += 1

    return dist


def doecaPorNiveisColestrol(listaUtentes):
    dist = {}
    inf,sup = menorEmaiorColestrol(listaUtentes)
    for i in range(inf, sup, 10):
        dist[(i, i+9)] = 0

    for id,valor in listaUtentes["COLESTROL"].items():
        if listaUtentes["TEMDOENCA"][id] == "1":
            for inf1,sup1 in dist:
                if inf1 <= int(valor) <= sup1:
                    dist[(inf1,sup1)] += 1

    return dist


def menorEmaiorColestrol(listaUtentes):
    tempMenor = int(listaUtentes["COLESTROL"][0])
    tempMaior = int(listaUtentes["COLESTROL"][0])

    for id,valor in listaUtentes["COLESTROL"].items():
        if int(valor) <= tempMenor:
            tempMenor = int(valor)
        elif int(valor) >= tempMaior:
            tempMaior = int(valor)

    return tempMenor,tempMaior

def desenhaTableasColestrol(listaUtentes):
    table = PrettyTable()
    table.field_names = [f"[{inf},{sup}]" for inf, sup in listaUtentes.keys()]
    table.add_row([f"{valor}" for valor in listaUtentes.values()])
    print(table)

def desenhaTabelasSexo(listaUtentes):
    table = PrettyTable()
    table.field_names = ["Masculino", "Feminino"]
    table.add_row([listaUtentes["Masculino"], listaUtentes["Feminino"]])
    print(table)

def desenhaTabelaEscEt(listaUtentes):
    table = PrettyTable()
    table.field_names = [f"[{inf},{sup}]" for inf, sup in listaUtentes.keys()]
    table.add_row([f"{valor}" for valor in listaUtentes.values()])
    print(table)

main()