import json
import re
import sys

def parcer(ficheiro):
    text = []
    with open(ficheiro, "r") as file:
        first_line = file.readline().strip()

        pattern = r',(?![^{}]*\})'
        fields =  re.split(pattern, first_line)

        for line in file:
            lines = line.strip().split(",")
            text.append(lines)

        filtered = [s for s in fields if s != ""]
    return filtered,text

def tpc4(first_line, lines):
    regex = r"^(.+)\{(\d+)(?:,(\d+))?\}(?:::(sum|media))?$"

    for campos in first_line:
        match = re.match(regex, campos)

        if match:
            prefixo = match.group(1)
            min_val = int(match.group(2))
            max_val = int(match.group(3)) if match.group(3) else None
            operacao = match.group(4)

            if max_val == None:
                mylista(first_line, lines, prefixo, min_val) # Ex1
            elif operacao == None:
                myintervalo(first_line, lines, prefixo, min_val, max_val) # Ex 2
            elif operacao == "sum":
                mysum(first_line, lines, prefixo, min_val, max_val)
            elif operacao == "media":
                media(first_line, lines, prefixo, min_val, max_val)


def mylista(first_line, lines, prefixo, min_val):
    static_fields = []
    for campo in first_line[:-1]:
        static_fields.append((campo, ""))
    static_fields.append((prefixo, ""))

    resultado = []
    i, l = 0, len(lines[0])
    for list in lines:
        dic = dict(static_fields)
        for elemento in list:
            coluna, valor = static_fields[i]
            dic[coluna] = elemento
            if i == l-min_val:
                dic[coluna] = [int(x) for x in list[-min_val:]]
                break
            i += 1
        i = 0
        resultado.append(dic)

    with open("alunos1.json", "w") as f:
        json.dump(resultado, f)
    print("Ficheiro alunos1.json escrito com sucesso")


def myintervalo(first_line, lines, prefixo, min_val, max_val):
    static_fields = []
    for campo in first_line[:-1]:
        static_fields.append((campo, ""))
    static_fields.append((prefixo, ""))

    resultado = []
    i, l = 0, len(lines[0])
    for list in lines:
        dic = dict(static_fields)
        for elemento in list:
            coluna, valor = static_fields[i]
            dic[coluna] = elemento
            if i == l - max_val:
                dic[coluna] = [int(x) for x in list[i:i+max_val] if x != ""]
                break
            i += 1
        i = 0
        resultado.append(dic)

    with open("alunos2.json", "w") as f:
        json.dump(resultado, f)
    print("Ficheiro alunos2.json escrito com sucesso")


def mysum(first_line, lines, prefixo, min_val, max_val):
    static_fields = []
    for campo in first_line[:-1]:
        static_fields.append((campo, ""))
    static_fields.append((prefixo, ""))

    resultado = []
    i, l = 0, len(lines[0])
    for list in lines:
        dic = dict(static_fields)
        for elemento in list:
            coluna, valor = static_fields[i]
            dic[coluna] = elemento
            if i == l - max_val:
                valores = [int(x) for x in list[i:i + max_val] if x != ""]
                dic[coluna] = sum(valores)
                break
            i += 1
        i = 0
        resultado.append(dic)

    with open("alunos3.json", "w") as f:
        json.dump(resultado, f)
    print("Ficheiro alunos3.json escrito com sucesso")


def media(first_line, lines, prefixo, min_val, max_val):
    static_fields = []
    for campo in first_line[:-1]:
        static_fields.append((campo, ""))
    static_fields.append((prefixo, ""))

    resultado = []
    i, l = 0, len(lines[0])
    for list in lines:
        dic = dict(static_fields)
        for elemento in list:
            coluna, valor = static_fields[i]
            dic[coluna] = elemento
            if i == l - max_val:
                valores = [int(x) for x in list[i:i + max_val] if x != ""]
                dic[coluna] = sum(valores)/len(valores)
                break
            i += 1
        i = 0
        dic["Media"] = dic["Notas"]
        del dic["Notas"]
        resultado.append(dic)
    
    #print(resultado)
    with open("alunos4.json", "w") as f:
        json.dump(resultado, f)
    print("Ficheiro alunos4.json escrito com sucesso")

if __name__ == "__main__":
    ficheiro = sys.argv[1]

    fst, lines = parcer(ficheiro)
    tpc4(fst, lines)

