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

CREATE_TABLES = """
CREATE TABLE IF NOT EXISTS pessoas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);
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