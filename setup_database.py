import psycopg2
from pyscopg2 import sql

# estabelecendo uma conexao com o banco de dados
# porta de comunicação do PostgreSQL, por padrão é 5432

config = {
	"user": "postgres",
	"password": "adm123",
	"host": "127.0.0.1",
	"port": "5432",
	"database": "database_name"
}
# Script para criação da tabela com alguns valores já inclusos
CREATE_TABLES = """
    CREATE TABLE Pessoa (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        pais_origem VARCHAR(50),
        telefone VARCHAR(20),
        data_nascimento DATE,
        cargo VARCHAR(50)
    );

    CREATE TABLE Juiz (
        pessoa_id INTEGER PRIMARY KEY,
        data_inicio DATE,
        FOREIGN KEY (pessoa_id) REFERENCES Pessoa(id)
    );

    INSERT INTO Pessoa (id, nome, pais_origem, cargo)
    VALUES 
    (1, 'João Silva', 'Brasil', 'Chef Executivo'),
    (2, 'Maria Garcia', 'Espanha', 'Crítica Gastronômica'),
    (3, 'Peter Jones', 'Estados Unidos', 'Mestre Churrasqueiro');

    INSERT INTO Juiz (pessoa_id, data_inicio)
    VALUES 
    (1, '2020-09-12'),
    (2, '2010-03-15'),
    (3, '2019-11-30');
"""

def setup_database():
    try:
        conexao = psycopg2.connect(**config)
        cursor = conexao.cursor()
        
        cursor.execute(CREATE_TABLES)
        conexao.commit()
        
        print("Tabelas criadas com sucesso!")
    
    except Exception as e:
        print("Erro ao criar tabelas:", e)
    
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

if __name__ == "__main__":
    setup_database()