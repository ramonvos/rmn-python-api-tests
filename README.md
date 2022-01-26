# Testes de Api em Python usando Pytest

Framework de automatização de testes de api em Python usando o Pytest

## Clonar o projeto

Clone o repositório no seu ambiente local

```bash
https://github.com/ramonvos/rmn-python-api-tests.git
```

## Instalação

Instalar o venv para criar ambiente virtual
```bash
pip install virtualenv
```

Criar um ambiente virtual

```bash
virtualenv _env
```

Acessar o ambiente virtual

```bash
_env\Scripts\activate
```

Instalar a biblioteca requests

```bash
pip install requests
```

Instalar a biblioteca pytest

```bash
pip install pytest
```

Instalar a biblioteca jsonpath

```bash
pip install jsonpath
```

Instalar a biblioteca Allure
```bash
pip install allure-pytest
```



## Execução

Execute o comando abaixo para executar todos os testes

```bash
pytest -s
```

## Execução com Allure 
Executar os testes e gerar arquivos Allure
```bash
pytest -s --alluredir=./temp/AllureResults
```
Executar os testes e gerar arquivos Allure
```bash
allure serve ./temp/AllureResults
```