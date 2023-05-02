# Prova para QA Automation Engineer

A avaliação para a vaga de QA Automation Engineer consiste na criação de scripts de teste automatizado baseados nos casos de testes desta página:
https://practicetestautomation.com/practice-test-login/

---
### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Python](https://www.python.org/downloads/). Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

---
## Dependências

Todas as dependências utilizadas no projeto, estão salvas no arquivo requirements.txt

```bash
pip install -r requirements.txt
```

## Execução dos casos de tests
---
Acesse a pasta "tests". No diretório, existirá uma pasta chamada "login" com os 3 scripts de teste para cada caso de teste.

```bash
cd tests\login
```
Para execução de todos os casos de testes, execute o seguinte comdando:

```bash
pytest pytest -v -s
```

ou execução de um caso de teste especifico, uma unidade, exemplo:

```bash
pytest -v -s .\test_negative_password.py
```

## Geração do relatorio dos testes

Dentro da pasta de tests, execute o camando abaixo, e gerará o html report de todos os casos de testes dentro da pasta, para abrir basta clicar em "Abrir com Browser" ou em 
um navagador de sua preferência:

```bash
pytest -v -s --html=AutomationPageObjectReport.html
```