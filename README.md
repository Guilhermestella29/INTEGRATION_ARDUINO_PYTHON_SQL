# Sensor de Temperatura com Arduino e PostgreSQL

Este é um projeto simples que lê dados de temperatura de um sensor conectado a um Arduino e os armazena em um banco de dados PostgreSQL. O código está escrito em Python e usa as bibliotecas `serial` para comunicação serial e `psycopg2` para interagir com o banco de dados.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados antes de executar o código:

- Python (versão X.X ou superior): [https://www.python.org/](https://www.python.org/)
- PostgreSQL: [https://www.postgresql.org/](https://www.postgresql.org/)
- Arduino IDE: [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)

## Configuração do Ambiente

1. Clone o repositório:

    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/Guilhermestella29/INTEGRATION_ARDUINO_PYTHON_SQL)
    ```

2. Instale as dependências Python:

    ```bash
    pip install psycopg2
    ```

3. Conecte o Arduino ao sensor de temperatura e certifique-se de que esteja funcionando corretamente.

4. Execute o código Python:

    ```bash
    python temperatura.py
    ```

## Configuração do Banco de Dados

1. Crie um banco de dados PostgreSQL chamado `io_py`.

    ```sql
    CREATE DATABASE io_py;
    ```

2. Crie uma tabela chamada `Dados_Temperatura`:

    ```sql
    CREATE TABLE Dados_Temperatura (
        id SERIAL PRIMARY KEY,
        registro TIMESTAMP,
        valor VARCHAR(15)
    );
    ```

## Execução

Execute o script Python para começar a ler dados da porta serial e inserir no banco de dados PostgreSQL.

```bash
python temperatura.py
