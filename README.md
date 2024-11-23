# Análise e Validação de Dados de eSports (League of Legends)

<div align="center">
  <img src="assets/banner-repositorio-postgresql-python-data-test-lol-esports.png" />
</div>

Este projeto realiza a análise e validação de dados de eSports relacionados ao jogo League of Legends. Utiliza Python, SQL e ferramentas de teste automatizado para garantir a integridade e qualidade dos dados.

## Índice

1. [Tecnologias Utilizadas](#1-tecnologias-utilizadas)
2. [Pré-requisitos](#2-pré-requisitos)
3. [Instalação e Configuração](#3-instalação-e-configuração)
    1. [Instalar as Dependências](#31-instalar-as-dependências)
    2. [Configuração do Banco de Dados](#32-configuração-do-banco-de-dados)
4. [Executando os Testes](#4-executando-os-testes)
5. [Contribuindo](#5-contribuindo)

## 1. Tecnologias Utilizadas

- **Python 3.10**: Linguagem de programação utilizada para manipulação dos dados e execução de testes.
- **SQLAlchemy**: Biblioteca para interação com o banco de dados PostgreSQL.
- **Pandas**: Usada para manipulação e análise de dados.
- **Pytest**: Framework de testes utilizado para validar os dados.

## 2. Pré-requisitos

- Python 3.7 ou superior
- Conta no Telegram e criação de um Bot
- Acesso ao repositório GitHub para configurar a automação

## 3. Instalação e Configuração

### 3.1 Instalar as Dependências

Instale as dependências necessárias utilizando o pip:

```bash
pip install -r requirements.txt
```

### 3.2 Configuração do Banco de Dados

Este projeto utiliza PostgreSQL. Configure a conexão com o banco de dados no arquivo config/db_config.py alterando as variáveis de conexão conforme sua necessidade.

*O projeto também inclui uma pasta chamada data, que contém um arquivo .csv com os dados necessários para a automação. Para garantir que as consultas SQL e os testes sejam realizados corretamente, é necessário importar este arquivo CSV para o banco de dados PostgreSQL.*

## 4. Executando os Testes

Os testes podem ser executados utilizando o pytest:

```bash
pytest tests/
```

Este comando irá rodar os testes de validação de dados, como a verificação de tabelas, colunas, dados nulos e negativos.

## 5. Contribuindo
Se você deseja apoiar este projeto, deixe um ⭐.

___

Feito com 💙 por [Marco Antonio](https://www.linkedin.com/in/mrk-silva/).