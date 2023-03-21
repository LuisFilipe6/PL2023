import re
import sys

#0 => pousada
#1 => LEVANTADA
#2 => IN CALL
#500 => ERRO

class Telefone:
    status = 0
    moedasExistentes = [1, 2, 5, 10, 20, 50, 100, 200]
    dinheiroAtual = 0

    def handle_moedas(self, moedas):
        m = re.compile("\d*[ce]")
        naoExistentes = []
        for moeda in m.findall(moedas):
            moedaOriginal = moeda
            print(moeda + " <=> " + moedaOriginal)
            if 'e' in moeda:
                moeda = int(moeda.replace("e", "")) * 100
            moeda = int(moeda.replace("c", ""))
            if moeda in self.moedasExistentes:
                self.dinheiroAtual += moeda
            else:
               naoExistentes.append(moedaOriginal)

        if len(naoExistentes) > 0:
            return f'{",".join(naoExistentes)} - moeda inválida; saldo = {self.getSaldo()}'
        else:
            return f'saldo = {self.getSaldo()}'

    def getSaldo(self):
        euros = int(self.dinheiroAtual/100)
        cents = self.dinheiroAtual%100
        return f'{euros:0d}e{cents:02d}c'

    def getTroco(self):
        restante = self.dinheiroAtual
        moedas = {'2e': 0, '1e': 0, '50c': 0, '20c': 0, '10c': 0, '5c': 0, '2c': 0, '1c': 0}
        while restante > 0:
            if restante >= 200:
                moedas['2e'] += 1
                restante -= 200
            if restante >= 100:
                moedas['1e'] += 1
                restante -= 100
            if restante >= 50:
                moedas['50c'] += 1
                restante -= 50
            if restante >= 20:
                moedas['20c'] += 1
                restante -= 20
            if restante >= 10:
                moedas['10c'] += 1
                restante -= 10
            if restante >= 5:
                moedas['5c'] += 1
                restante -= 5
            if restante >= 2:
                moedas['2c'] += 1
                restante -= 2
            if restante >= 1:
                moedas['1c'] += 1
                restante -= 1
        return ','.join([str(value) + "x" + str(key) for key,value in moedas.items() if value > 0])

    def gastaDinheiro(self, valor):
        if self.dinheiroAtual - valor > 0:
            self.dinheiroAtual -= valor
            return True
        return False

    def handle_chamada(self, chamada):
        numero = chamada.replace("T=", "")

        handle_loc = re.search("\d*", numero)
        handle_int = re.search("00\d*", numero)
        if handle_int:
            if self.gastaDinheiro(150):
                status = 2
                return "saldo = " + self.getSaldo()
            else:
                return "Não dispõe de dinheiro para efetuar a chamada."
        if handle_loc and len(handle_loc.group(0)) == 9:
            handle_loc = handle_loc.group(0)
            print(handle_loc[:4])
            if (handle_loc[:3] == "601" or handle_loc[:3] == "641") and not self.gastaDinheiro(10):
                return "Esse número não é permitido neste telefone. Queira discar novo número!"
            if handle_loc[:3] == "808" and not self.gastaDinheiro(10):
                return "Não dispõe de dinheiro para efetuar a chamada."
            if handle_loc[:1] == "2" and not self.gastaDinheiro(25):
                return "Não dispõe de dinheiro para efetuar a chamada."
            status = 2
            return "saldo = " + self.getSaldo()
        return "Esse número não é permitido neste telefone. Queira discar novo número!"

    def handle_levantar(self):
        if self.status != 1:
            self.status = 1
            return "Introduza moedas."

    def handle_pousar(self):
        self.status = 0
        return f'troco={self.getTroco()}; Volte sempre!'

    def handle_input(self, input):
        output = "maq: ERRO"
        if re.match("T=\d+", input):
            output = self.handle_chamada(input)
        if re.match("MOEDA \d*[ce]", input):
            output = self.handle_moedas(input)
        if input == "DINHEIRO":
            print(dinheiroAtual)
        if input == "LEVANTAR":
            output = self.handle_levantar()
        if input == "POUSAR":
            output = self.handle_pousar()
        if input == "ABORTAR":
            print("ABORTAR")
        return f'maq: "{output}"'

def main():
    print('maq: "Bem-vindo à cabine telefónica!"')
    t = Telefone()
    while True:
        line = input().strip()
        if not line:
            continue
        output = t.handle_input(line)
        print(output)
        if output == -1:
            print('maq: "Até a próxima ligação!"')
            break

if __name__ == "__main__":
    main()