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

CREATE_TABLES = """
    CREATE TABLE Pessoa (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        pais_origem VARCHAR(50),
        telefone VARCHAR(20),
        data_nascimento DATE
    );

    CREATE TABLE Juiz (
        pessoa_id INTEGER PRIMARY KEY,
        data_inicio DATE,
        cargo VARCHAR(50),
        FOREIGN KEY (pessoa_id) REFERENCES Pessoa(id)
    );

    INSERT INTO Pessoa (nome, pais_origem)
    VALUES 
    ('João Silva', 'Brasil'),
    ('Maria Garcia', 'Espanha'),
    ('Peter Jones', 'Estados Unidos');

    INSERT INTO Juiz (pessoa_id, data_inicio, cargo)
    VALUES 
    ('1', '2020-09-12', 'Chef Executivo'),
    ('2', '2010-03-15', 'Crítica Gastronômica'),
    ('3', '2019-11-30', 'Mestre Churrasqueiro');
"""
cursor.execute(CREATE_TABLES)
conexao.commit()
    
cursor.close()
conexao.close()
