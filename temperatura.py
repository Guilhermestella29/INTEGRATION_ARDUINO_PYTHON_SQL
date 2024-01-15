import serial
import psycopg2
import datetime

# Define a variavel com os dados da conexão com o PostgreSQL
conexao_parametros = {
    'dbname': 'io_py',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432'  # Porta padrão do PostgreSQL
}

# Iniciar a conexão serial 
conect = serial.Serial('/dev/ttyACM0', 9600)

#Loop e comandos a serem executados
while True:
    agora = datetime.datetime.now()
    now = agora.strftime('%d/%m/%Y')
    try:
        # Leitura da porta serial e tratamento dos dados
        linha = str(conect.readline())
        t = linha[2:7]
        print(now)
        print(t)

    except Exception as e:
        print("Erro ao ler da porta serial:", e)

    try:
        conexao = psycopg2.connect(**conexao_parametros) #Efetua a conexão com o banco de dados
        print("Conexão bem-sucedida com o Banco de Dados!\n")

        dados_insert = "INSERT INTO Dados_Temperatura (valor, registro) VALUES (%s, %s)"
        
        cursor = conexao.cursor()
        cursor.execute(dados_insert, (t, now))

        conexao.commit()
        print(cursor.rowcount, "Dados de Registro e Temperetura inseridos com sucesso no Banco!\n")
    

    except psycopg2.Error as e:
        print("Erro ao conectar ao PostgreSQL:", e)

    finally:
        if conexao:
            conexao.close()
            print("Conexão com Banco de Dados fechada!\n")


# Fechar a conexão serial (será executado apenas se o loop for interrompido)
conect.close()
