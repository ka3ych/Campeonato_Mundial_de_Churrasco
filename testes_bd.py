# -*- coding: utf-8 -*-
import psycopg2
from psycopg2 import sql

# estabelecendo uma conexao com o banco de dados
# porta de comunicação do PostgreSQL, por padrão é 5432
# user, senha, e database modificamo conforme configurado na nossa própria máquina

conexao = psycopg2.connect (
	user="postgres",
	password="admin123",
	host="127.0.0.1",
	port="5432",
	database="churras"
)
# Script para criação apenas da tabela de Pessoa e de Juízes para que a lógica na aplicação possa ser feita tabela com alguns valores já inclusos

cursor = conexao.cursor()

sql = """
SELECT 
    p.id, 
    p.nome, 
    p.pais_origem, 
    j.cargo, 
    j.data_inicio
FROM 
    Pessoa p
JOIN 
    Juiz j ON p.id = j.pessoa_id
ORDER BY 
    p.id ASC;
"""

cursor.execute(sql)

dados = cursor.fetchall() 

all_data = []
for id, nome, pais, cargo, data in dados:
    data_formatada = data.strftime('%d/%m/%Y')
    
    all_data.append((id, nome, pais, cargo, data_formatada))

if dados:
    print(all_data)
else:
    print('Não foi possível carregar todos os registros.')

conexao.commit()
    
cursor.close()
conexao.close()
