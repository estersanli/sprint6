# Sprint 6 - Sistema Bancário

## Descrição

Este projeto foi desenvolvido em Python utilizando Programação Orientada a Objetos.

O sistema simula contas bancárias e utiliza conceitos como:

- Classes
- Objetos
- Herança
- Encapsulamento
- Polimorfismo
- Classe abstrata
- Propriedades
- Tratamento de exceções
- Métodos especiais

## Classes

O projeto possui quatro classes:

- Cliente
- Conta
- ContaCorrente
- ContaPoupanca

A classe Conta é abstrata e não pode ser criada diretamente.

## Diagrama de Classes



classDiagram

class Cliente { -nome -email +Cliente(nome, email) +str() }

class Conta { <<abstract>> -numero -saldo -cliente +Conta(numero, cliente, saldo) +depositar(valor) +sacar(valor) +calcularrendimento() +str() +repr() +eq_() }

class ContaCorrente { +ContaCorrente(numero, cliente, saldo) +calcularrendimento() +str_() }

class ContaPoupanca { +ContaPoupanca(numero, cliente, saldo) +calcularrendimento() +str_() }

Conta <|-- ContaCorrente Conta <|-- ContaPoupanca Conta --> Cliente


## Herança

A classe `Conta` é a classe principal.

`ContaCorrente` e `ContaPoupanca` herdam dela porque são tipos de conta.

Foi utilizado `super()` para chamar o construtor da classe `Conta`.

## Encapsulamento

Foram utilizadas propriedades com `@property`.

O saldo não pode ser negativo.

O número da conta também precisa ser maior que zero.

O nome do cliente não pode ficar vazio.

O e-mail precisa seguir um formato válido.

## Polimorfismo

As classes `ContaCorrente` e `ContaPoupanca` possuem o mesmo método:



calcular_rendimento()


Porém, cada uma calcula o rendimento de uma maneira diferente.

A conta corrente utiliza 1%.

A conta poupança utiliza 5%.

Dessa forma, podemos percorrer uma lista contendo os dois tipos de conta e chamar o mesmo método.

## Métodos especiais

Foram utilizados:

- `__str__()` para mostrar os objetos de forma amigável.
- `__repr__()` para representar os objetos.
- `__eq__()` para comparar duas contas.

## Tratamento de erros

O programa utiliza `try/except` para tratar situações inválidas.

Exemplos:

- Saque maior que o saldo.
- E-mail inválido.
- Valor inválido para depósito.
- Valor inválido para saque.
- Saldo negativo.

## Objetos criados

O programa cria 5 clientes e 10 contas.

Existem contas correntes e contas poupança.

Isso permite demonstrar o polimorfismo utilizando objetos de classes diferentes.

## Exemplo de saída



===== CONTAS =====

Conta Corrente: 1 | Cliente: Ana | Saldo: R$ 1000.00 Conta Corrente: 2 | Cliente: Bruno | Saldo: R$ 1500.00 Conta Poupança: 4 | Cliente: Daniel | Saldo: R$ 2000.00

===== RENDIMENTOS =====

Conta 1: Rendimento = R$ 10.00 Conta 2: Rendimento = R$ 15.00 Conta 4: Rendimento = R$ 100.00


## Como executar

Abra o terminal na pasta do projeto e execute:



python sistema_bancario.py


## Conclusão

O projeto demonstra os principais conceitos de Programação Orientada a Objetos em Python, utilizando uma situação simples de um sistema bancário.


:::

Estrutura final do GitHub
Sprint_6/
│
├── sistema_bancario.py
└── README.md

Checklist do enunciado
Requisito	Onde está
4 classes	Cliente, Conta, ContaCorrente, ContaPoupanca
Classe abstrata	Conta
ABC e @abstractmethod	Conta
__init__	Todas as classes
__str__	Todas as classes
@property	Cliente e Conta
Validação	Nome, e-mail, número e saldo
Herança	ContaCorrente e ContaPoupanca
super()	Classes filhas
Polimorfismo	calcular_rendimento()
__repr__	Cliente e Conta
__eq__	Conta
10 objetos	10 contas
try/except	Depósito, saque e e-mail
README	Incluído
Diagrama Mermaid	Incluído

Essa versão é simples de propósito, mas cobre os requisitos do Sprint 6 sem colocar recursos avançados que não seriam necessários para uma aluna no início do curso.
