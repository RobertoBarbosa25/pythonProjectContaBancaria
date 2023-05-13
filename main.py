class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= 500:
                if self.saldo >= valor:
                    if len(self.saques) < 3:
                        self.saldo -= valor
                        self.saques.append(valor)
                        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                    else:
                        print("Limite diário de saques atingido.")
                else:
                    print("Saldo insuficiente. Não é possível realizar o saque.")
            else:
                print("Valor de saque excede o limite de R$ 500.")
        else:
            print("O valor do saque deve ser positivo.")

    def extrato(self):
        print("Extrato:")
        print("Depósitos:")
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito:.2f}")

        print("Saques:")
        for saque in self.saques:
            print(f"Saque: R$ {saque:.2f}")

        print(f"Saldo atual: R$ {self.saldo:.2f}")


# Exemplo de uso
conta = ContaBancaria()
conta.depositar(100)
conta.sacar(50)
conta.sacar(200)
conta.depositar(300)
conta.extrato()