import re
import sys

#0 => pousada
#1 => LEVANTADA
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

    def handle_chamada(self, chamada):
        print("OI")

    def handle_input(self, input):
        output = "maq: ERRO"
        if re.match("T=\d+", input):
            output = self.handle_chamada(input)
            # Parse chamada
        if re.match("MOEDA \d*[ce]", input):
            output = self.handle_moedas(input)
            # Parse moedas
        if input == "DINHEIRO":
            print(dinheiroAtual)
        if input == "LEVANTAR":
            statusMaquina = LEVANTADA
        if input == "POUSAR":
            statusMaquina = POUSADA
        if input == "ABORTAR":
            print("ABORTAR")
            # Parse abortar
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