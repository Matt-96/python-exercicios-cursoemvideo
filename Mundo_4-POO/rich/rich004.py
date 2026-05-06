from rich import print
from rich import inspect

# Declaração de Classe
class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0): # Método Construtor
        self.Id = id
        self.titular = nome
        self.saldo =  saldo
        print(f"Conta {self.Id} criada com sucesso! Saldo atual de {self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.Id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.Id}.")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.Id}: SALDO INSUFICIENTE.")

        self.saldo -= valor
        print(f"Saque de {valor:,.2f} autorizado na conta {self.Id}")


# Declaração de Objetos

c1 = ContaBancaria(112, "Matheus", saldo=5000)
c1.depositar(500)
c1.sacar(200)

inspect(c1)