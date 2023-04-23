import os
import platform
import json
# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

class ComputerSell:
    def __init__(self, computer_type, price):
        self.type = computer_type
        self.price = price

    def installment_criteria(self):
        if self.price >= 1000 and self.price < 5000:
            return 'Você pode parcelar em até 6x sem juros!'
        elif self.price >= 5000 and self.price < 10000:
            return 'Você pode parcelar em até 12x sem juros!'
        elif self.price >= 10000:
            return 'Você pode parcelar em até 24x sem juros!'
        else:
            return 'Não foi possível parcelar pois o valor está abaixo do nosso critério de parcelamento. Favor, falar com o vendedor!'
    
    def to_dict(self):
        return {
            'type': self.type,
            'price': self.price,
            'installment_criteria': self.installment_criteria(),
        }

# Limpa console para ficar mais intuitivo no terminal    
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Convertendo as instâncias da classe em uma lista
computers = [
    ComputerSell('Notebook', 1200),
    ComputerSell('PC Gamer', 6540),
    ComputerSell('Servidor', 32131),
]

# Loop for para salvar em arquivos .json diferentes
for i, computer in enumerate(computers, 1):
    filename = f'computer{i}.json'
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(computer.to_dict(), file, ensure_ascii=False, indent=4)

# Cheque os arquivos .json que foram gerados com a execução do programa!