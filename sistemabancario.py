from abc import ABC, abstractmethod
import re


class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if nome == "":
            raise ValueError("O nome não pode ficar vazio.")
        self._nome = nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(padrao, email):
            raise ValueError("E-mail inválido.")

        self._email = email

    def __str__(self):
        return f"Cliente: {self.nome} | E-mail: {self.email}"

    def __repr__(self):
        return f"Cliente('{self.nome}', '{self.email}')"


class Conta(ABC):
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        if numero <= 0:
            raise ValueError("Número da conta inválido.")
        self._numero = numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")

        self._saldo -= valor

    @abstractmethod
    def calcular_rendimento(self):
        pass

    def __str__(self):
        return (
            f"Conta: {self.numero} | "
            f"Cliente: {self.cliente.nome} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )

    def __repr__(self):
        return f"Conta({self.numero}, {self.saldo})"

    def __eq__(self, outra):
        return self.numero == outra.numero


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo=0):
        super().__init__(numero, cliente, saldo)

    def calcular_rendimento(self):
        return self.saldo * 0.01

    def __str__(self):
        return (
            f"Conta Corrente: {self.numero} | "
            f"Cliente: {self.cliente.nome} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, saldo=0):
        super().__init__(numero, cliente, saldo)

    def calcular_rendimento(self):
        return self.saldo * 0.05

    def __str__(self):
        return (
            f"Conta Poupança: {self.numero} | "
            f"Cliente: {self.cliente.nome} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )


clientes = [
    Cliente("Ana", "ana@gmail.com"),
    Cliente("Bruno", "bruno@gmail.com"),
    Cliente("Carla", "carla@gmail.com"),
    Cliente("Daniel", "daniel@gmail.com"),
    Cliente("Eduarda", "eduarda@gmail.com")
]


contas = [
    ContaCorrente(1, clientes[0], 1000),
    ContaCorrente(2, clientes[1], 1500),
    ContaCorrente(3, clientes[2], 800),
    ContaPoupanca(4, clientes[3], 2000),
    ContaPoupanca(5, clientes[4], 3000),
    ContaCorrente(6, clientes[0], 500),
    ContaPoupanca(7, clientes[1], 1200),
    ContaCorrente(8, clientes[2], 700),
    ContaPoupanca(9, clientes[3], 2500),
    ContaCorrente(10, clientes[4], 900)
]


print(" CONTAS ")

for conta in contas:
    print(conta)


print("\n RENDIMENTOS ")

for conta in contas:
    rendimento = conta.calcular_rendimento()

    print(
        f"Conta {conta.numero}: "
        f"Rendimento = R$ {rendimento:.2f}"
    )


print("\n DEPÓSITO ")

try:
    contas[0].depositar(500)

    print(contas[0])

except ValueError as erro:
    print(f"Erro: {erro}")


print("\n SAQUE ")

try:
    contas[1].sacar(300)

    print(contas[1])

except ValueError as erro:
    print(f"Erro: {erro}")


print("\n TESTE DE ERRO ")

try:
    contas[2].sacar(5000)

except ValueError as erro:
    print(f"Erro: {erro}")


print("\n TESTE DE E-MAIL ")

try:
    cliente_teste = Cliente("Teste", "email_invalido")

except ValueError as erro:
    print(f"Erro: {erro}")


print("\n COMPARAÇÃO ")

if contas[0] == contas[1]:
    print("As contas são iguais.")
else:
    print("As contas são diferentes.")