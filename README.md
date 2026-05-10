# Sistema Bancário Simples em Python

Este projeto é uma aplicação simples desenvolvida em **Python** que simula operações básicas de uma conta bancária através do terminal.

O objetivo principal é praticar conceitos fundamentais de programação como:

* Estruturas de controlo (`if`, `while`)
* Funções
* Validação de dados
* Tratamento de erros com `try/except`
* Organização de código

---

# Funcionalidades

O sistema apresenta um menu interativo com as seguintes opções:

**1 - Depositar**
Permite adicionar dinheiro à conta. O programa valida se o valor introduzido é um número válido e se é maior que zero.

**2 - Levantar**
Permite retirar dinheiro da conta, verificando:

* se o valor é válido
* se o saldo é suficiente

**3 - Ver saldo**
Mostra o saldo atual disponível na conta.

**4 - Sair**
Encerra o programa de forma segura.

---

# Validação de Dados

O programa inclui validação para evitar erros comuns do utilizador:

* Impede inserir **letras ou texto** onde é esperado um número
* Impede valores **negativos ou iguais a zero**
* Impede levantar dinheiro **acima do saldo disponível**

Essas verificações são feitas utilizando **tratamento de exceções (`try/except`)**.

---

# Como Executar

## 1️⃣ Pré-requisitos

Ter o **Python 3.x** instalado no computador.

## 2️⃣ Executar o programa

1. Guarda o código num ficheiro chamado:

```
banco.py
```

2. Abre o terminal na pasta do projeto.

3. Executa o comando:

```
python banco.py
```

4. Escolhe uma das opções apresentadas no menu.

---

# Exemplo de Execução

```
=== Conta do Banco ===
1 - Depositar
2 - Levantar
3 - Ver saldo
4 - Sair

Escolha uma opção: 1
Quanto queres depositar? 100
Depósito feito com sucesso!
```

---

# Estrutura do Código

O programa está dividido em várias funções para melhorar a organização:

* `menu()` → mostra o menu
* `ler_menu()` → valida a opção escolhida pelo utilizador
* `depositar(saldo)` → adiciona dinheiro ao saldo
* `levantar(saldo)` → remove dinheiro do saldo
* `ver_saldo(saldo)` → mostra o saldo atual
* `main()` → controla o fluxo principal do programa

---

# Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas:

* Guardar o saldo em **ficheiro** para não perder dados ao fechar o programa
* Criar **histórico de transações**
* Implementar **interface gráfica**
* Criar uma **API ou versão web**
* Adicionar **tipagem (`type hints`)** no código

---

# Objetivo do Projeto

Este projeto foi criado como exercício para praticar programação em Python e desenvolver pensamento lógico na construção de pequenos sistemas.

Ele pode servir como base para projetos mais avançados no futuro.
