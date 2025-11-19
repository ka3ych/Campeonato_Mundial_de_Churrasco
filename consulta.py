"""
Integrantes:
Alisson Santos Silva - 15642794
Dérick dos Santos Arriado - 15636042
João Henrique Kuroki Cominato - 15462870
Karina Yang Chen - 15466658

É necessário instalar a psycopg2, então precisa escrever no terminal:
'pip install psycopg2'
Para o programa rodar
"""

import datetime
import psycopg2
from psycopg2 import Error

class GerenciadorBanco:
    """Aqui abaixo temos tudo que vai ser usado para fazer a consulta do banco de dados"""
    def __init__(self):
        self.connection = None
        self.cursor = None

    def conectar(self):
        """
        Conecta ao banco de dados PostgreSQL
        """
        try:
            # Altere estas informações conforme sua configuração
            self.connection = psycopg2.connect(
                host="localhost",
                database="churras",  # Nome do seu banco
                user="postgres",             # Seu usuário
                password="admin123",            # Sua senha
                port='6932'            # Sua porta
            )
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados estabelecida com sucesso!")
            return True
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False

    def desconectar(self):
        """Desconecta do banco de dados"""
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Conexão com o banco de dados fechada.")

    def menu_principal(self):
        """Menu principal do programa"""
        while True:
            print("\n" + "="*50)
            print("SISTEMA DE GERENCIAMENTO - COMPETIÇÃO CULINÁRIA")
            print("="*50)
            print("1. Inserir dados")
            print("2. Listar dados")
            print("3. Atualizar dados")
            print("4. Remover dados")
            print("5. Consultas especiais")
            print("6. Sair")
            print("="*50)

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.menu_inserir()
            elif opcao == "2":
                self.menu_listar()
            elif opcao == "3":
                self.menu_atualizar()
            elif opcao == "4":
                self.menu_remover()
            elif opcao == "5":
                self.menu_consultas()
            elif opcao == "6":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_inserir(self):
        """Menu para inserir dados nas tabelas"""
        while True:
            print("\n--- INSERIR DADOS ---")
            print("1. Inserir país")
            print("2. Inserir equipe")
            print("3. Inserir patrocinador")
            print("4. Inserir pessoa")
            print("5. Inserir juiz")
            print("6. Inserir competidor")
            print("7. Inserir prova")
            print("8. Inserir ingrediente")
            print("9. Inserir corte de carne")
            print("10. Inserir critério")
            print("11. Inserir avaliação de prova")
            print("12. Inserir avalição do avaliador")
            print("13. Inserir avaliação do critério")
            print("14. Inserir patrocínio")
            print("15. Inserir ingredientes da prova")
            print("16. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir_pais()
            elif opcao == "2":
                self.inserir_equipe()
            elif opcao == "3":
                self.inserir_patrocinador()
            elif opcao == "4":
                self.inserir_pessoa()
            elif opcao == "5":
                self.inserir_juiz()
            elif opcao == "6":
                self.inserir_competidor()
            elif opcao == "7":
                self.inserir_prova()
            elif opcao == "8":
                self.inserir_ingrediente()
            elif opcao == "9":
                self.inserir_corte_carne()
            elif opcao == "10":
                self.inserir_criterio()
            elif opcao == "11":
                self.inserir_avaliacao_prova()
            elif opcao == "12":
                self.inserir_avaliacao_avaliador()
            elif opcao == "13":
                self.inserir_avaliacao_criterio()
            elif opcao == "14":
                self.inserir_patrocina()
            elif opcao == "15":
                self.inserir_possui()
            elif opcao == "16":
                return
            else:
                print("Opção inválida!")

    def menu_listar(self):
        """Menu para listar dados das tabelas"""
        while True:
            print("\n--- LISTAR DADOS ---")
            print("1. Listar países")
            print("2. Listar equipes")
            print("3. Listar patrocinadores")
            print("4. Listar pessoas")
            print("5. Listar juízes")
            print("6. Listar competidores")
            print("7. Listar provas")
            print("8. Listar ingredientes")
            print("9. Listar cortes de carne")
            print("10. Listar critérios")
            print("11. Listar avaliações da prova")
            print("12. Listar avalições do avaliador")
            print("13. Listar avaliações de critério")
            print("14. Listar patrocínios")
            print("15. Listar ingredientes da prova")
            print("16. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar_paises()
            elif opcao == "2":
                self.listar_equipes()
            elif opcao == "3":
                self.listar_patrocinadores()
            elif opcao == "4":
                self.listar_pessoas()
            elif opcao == "5":
                self.listar_juizes()
            elif opcao == "6":
                self.listar_competidores()
            elif opcao == "7":
                self.listar_provas()
            elif opcao == "8":
                self.listar_ingredientes()
            elif opcao == "9":
                self.listar_cortes_carne()
            elif opcao == "10":
                self.listar_criterios()
            elif opcao == "11":
                self.listar_avaliacoes_prova()
            elif opcao == "12":
                self.listar_avaliacoes_avaliador()
            elif opcao == "13":
                self.listar_avaliacoes_criterio()
            elif opcao == "14":
                self.listar_patrocina()
            elif opcao == "15":
                self.listar_possui()
            elif opcao == "16":
                return
            else:
                print("Opção inválida!")

    def menu_atualizar(self):
        """Menu para atualizar dados"""
        while True:
            print("\n--- ATUALIZAR DADOS ---")
            print("1. Atualizar equipe")
            print("2. Atualizar pessoa")
            print("3. Atualizar patrocinador")
            print("4. Atualizar prova")
            print("5. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.atualizar_equipe()
            elif opcao == "2":
                self.atualizar_pessoa()
            elif opcao == "3":
                self.atualizar_patrocinador()
            elif opcao == "4":
                self.atualizar_prova()
            elif opcao == "5":
                return
            else:
                print("Opção inválida!")

    def menu_remover(self):
        """Menu para remover dados"""
        while True:
            print("\n--- REMOVER DADOS ---")
            print("1. Remover país")
            print("2. Remover equipe")
            print("3. Remover pessoa")
            print("4. Remover patrocinador")
            print("5. Remover juiz")
            print("6. Remover competidor")
            print("7. Remover ingrediente")
            print("8. Remover corte de carne")
            print("9. Remover critério")
            print("10. Remover avaliação de prova")
            print("11. Remover prova")
            print("12. Remover patrocínio")
            print("13. Remover avaliação do avaliador")
            print("14. Remover avaliação de critério")
            print("15. Remover associação de ingrediente na prova")
            print("16. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.remover_pais()
            elif opcao == "2":
                self.remover_equipe()
            elif opcao == "3":
                self.remover_pessoa()
            elif opcao == "4":
                self.remover_patrocinador()
            elif opcao == "5":
                self.remover_juiz()
            elif opcao == "6":
                self.remover_competidor()
            elif opcao == "7":
                self.remover_ingrediente()
            elif opcao == "8":
                self.remover_cortes_carne()
            elif opcao == "9":
                self.remover_criterio()
            elif opcao == "10":
                self.remover_avaliacao_prova()
            elif opcao == "11":
                self.remover_prova()
            elif opcao == "12":
                self.remover_patrocina()
            elif opcao == "13":
                self.remover_avaliacao_avaliador()
            elif opcao == "14":
                self.remover_avaliacao_criterio()
            elif opcao == "15":
                self.remover_possui()
            elif opcao == "16":
                return
            else:
                print("Opção inválida!")

    def menu_consultas(self):
        """Menu para consultas especiais"""
        while True:
            print("\n--- CONSULTAS ESPECIAIS ---")
            print("1. País, Equipes e Competidores")
            print("2. Equipes sem competidores (SELECT aninhado)")
            print("3. Ingredientes que não estão sendo usados em provas (SELECT aninhado)")
            print("4. Equipes com mais competidores (função de grupo)")
            print("5. Média de notas por juiz (função de grupo)")
            print("6. Diferença: provas com e sem ingredientes específicos (operador de conjunto)")
            print("7. União: patrocinadores ativos e ingredientes patrocinados (operador de conjunto)")
            print("8. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.consulta_pais_equipes_integrantes()
            elif opcao == "2":
                self.consulta_equipes_sem_competidores()
            elif opcao == "3":
                self.consulta_ingredientes_nao_utilizados()
            elif opcao == "4":
                self.consulta_equipes_mais_competidores()
            elif opcao == "5":
                self.consulta_media_notas_juiz()
            elif opcao == "6":
                self.consulta_diferenca_provas_ingredientes()
            elif opcao == "7":
                self.consulta_uniao_patrocinadores_ingredientes()
            elif opcao == "8":
                return
            else:
                print("Opção inválida!")

    # MÉTODOS PARA INSERIR DADOS
    def inserir_pais(self):
        try:
            print("\n--- INSERIR PAÍS ---")
            nome_pais = input("Nome do país: ")

            query = "INSERT INTO pais (nome_pais) VALUES (%s)"
            self.cursor.execute(query, (nome_pais,))
            self.connection.commit()
            print("País inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir país: {e}")

    def inserir_equipe(self):
        try:
            print("\n--- INSERIR EQUIPE ---")
            nome_equipe = input("Nome da equipe: ")
            self.listar_paises()
            id_pais = input("ID do país: ")

            query = "INSERT INTO equipe (nome_equipe, id_pais) VALUES (%s, %s)"
            self.cursor.execute(query, (nome_equipe, id_pais))
            self.connection.commit()
            print("Equipe inserida com sucesso!")
        except Error as e:
            print(f"Erro ao inserir equipe: {e}")

    def inserir_patrocinador(self):
        try:
            print("\n--- INSERIR PATROCINADOR ---")
            nome_patrocinador = input("Nome do patrocinador: ")
            descricao_patrocinador = input("Descrição: ")

            query = "INSERT INTO patrocinador (nome_patrocinador, descricao_patrocinador) VALUES (%s, %s)"
            self.cursor.execute(query, (nome_patrocinador, descricao_patrocinador))
            self.connection.commit()
            print("Patrocinador inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir patrocinador: {e}")

    def inserir_pessoa(self):
        try:
            print("\n--- INSERIR PESSOA ---")
            nome_primeiro = input("Primeiro nome: ")
            nome_ultimo = input("Último nome: ")
            numero_telefone = input("Número de telefone: ")
            data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
            print("Tipo: 1 - Juiz, 2 - Competidor")
            tipo = input("Tipo: ")

            query = "INSERT INTO pessoa (nome_primeiro, nome_ultimo, numero_telefone, data_nascimento, tipo) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (nome_primeiro, nome_ultimo, numero_telefone, data_nascimento, tipo))
            self.connection.commit()
            print("Pessoa inserida com sucesso!")
        except Error as e:
            print(f"Erro ao inserir pessoa: {e}")

    def inserir_juiz(self):
        try:
            print("\n--- INSERIR JUÍZ ---")
            self.listar_pessoas_juizes()
            id_pessoa = input("ID da pessoa: ")
            data_admissao = input("Data de admissão (YYYY-MM-DD): ")
            descricao_juiz = input("Descrição do juiz: ")

            query = "INSERT INTO juiz (id_pessoa, data_admissao, descricao_juiz) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (id_pessoa, data_admissao, descricao_juiz))
            self.connection.commit()
            print("Juiz inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir juiz: {e}")

    def inserir_competidor(self):
        try:
            print("\n--- INSERIR COMPETIDOR ---")
            self.listar_pessoas_competidores()
            self.listar_equipes()
            id_pessoa = input("\nID da pessoa: ")
            data_inscricao = input("Data de inscrição (YYYY-MM-DD): ")
            id_equipe = input("ID da equipe: ")

            query = "INSERT INTO competidor (id_pessoa, data_inscricao, id_equipe) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (id_pessoa, data_inscricao, id_equipe))
            self.connection.commit()
            print("Competidor inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir competidor: {e}")

    def inserir_prova(self):
        try:
            print("\n--- INSERIR PROVA ---")
            tempo = input("Tempo (HH:MM): ")
            dificuldade = input("Dificuldade (1-3): ")
            descricao_prova = input("Descrição da prova: ")

            query = "INSERT INTO prova (tempo, dificuldade, descricao_prova) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (tempo, dificuldade, descricao_prova))
            self.connection.commit()
            print("Prova inserida com sucesso!")
        except Error as e:
            print(f"Erro ao inserir prova: {e}")

    def inserir_ingrediente(self):
        try:
            print("\n--- INSERIR INGREDIENTE ---")
            nome_ingrediente = input("Nome do ingrediente: ")
            self.listar_patrocinadores()
            id_patrocinador = input("ID do patrocinador (ou deixe vazio): ") or None

            query = "INSERT INTO ingrediente (nome_ingrediente, id_patrocinador) VALUES (%s, %s)"
            self.cursor.execute(query, (nome_ingrediente, id_patrocinador))
            self.connection.commit()
            print("Ingrediente inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir ingrediente: {e}")

    def inserir_corte_carne(self):
        try:
            print("\n--- INSERIR CORTE DE CARNE ---")
            self.listar_ingredientes()
            id_ingrediente = input("ID do ingrediente: ")
            print("Tipo: 1 - Bovina, 2 - Suína, 3 - Frango, 4 - Outros")
            tipo = input("Tipo: ")
            descricao = input("Descrição: ")

            query = "INSERT INTO corte_carne (id_ingrediente, tipo, descricao) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (id_ingrediente, tipo, descricao))
            self.connection.commit()
            print("Corte de carne inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir corte de carne: {e}")

    def inserir_criterio(self):
        try:
            print("\n--- INSERIR CRITÉRIO ---")
            nome_criterio = input("Nome do critério: ")
            descricao_criterio = input("Descrição: ")
            pontuacao_maxima = input("Pontuação máxima: ")

            query = "INSERT INTO criterio (nome_criterio, descricao_criterio, pontuacao_maxima) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (nome_criterio, descricao_criterio, pontuacao_maxima))
            self.connection.commit()
            print("Critério inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir critério: {e}")

    def inserir_avaliacao_prova(self):
        try:
            print("\n--- INSERIR AVALIAÇÃO DE PROVA ---")
            self.listar_equipes()
            id_equipe = input("ID da equipe: ")
            data = input("Data da avaliação (YYYY-MM-DD): ")

            query = "INSERT INTO avaliacao_prova (id_equipe, data) VALUES (%s, %s)"
            self.cursor.execute(query, (id_equipe, data))
            self.connection.commit()
            print("Avaliação de prova inserida com sucesso!")
        except Error as e:
            print(f"Erro ao inserir avaliação de prova: {e}")
            
    def inserir_avaliacao_avaliador(self):
        try:
            print("\n--- INSERIR AVALIAÇÃO DO AVALIADOR ---")
            
            # Listar avaliações de prova disponíveis
            print("\nAvaliações de prova disponíveis:")
            query_avaliacoes = """
            SELECT ap.id_avaliacao, e.nome_equipe, ap.data 
            FROM avaliacao_prova ap 
            JOIN equipe e ON ap.id_equipe = e.id_equipe
            """
            self.cursor.execute(query_avaliacoes)
            avaliacoes = self.cursor.fetchall()
            for av in avaliacoes:
                print(f"ID: {av[0]} | Equipe: {av[1]} | Data: {av[2]}")
            
            # Listar juízes disponíveis
            print("\nJuízes disponíveis:")
            query_juizes = """
            SELECT j.id_pessoa, p.nome_primeiro, p.nome_ultimo 
            FROM juiz j 
            JOIN pessoa p ON j.id_pessoa = p.id_pessoa
            """
            self.cursor.execute(query_juizes)
            juizes = self.cursor.fetchall()
            for j in juizes:
                print(f"ID: {j[0]} | Nome: {j[1]} {j[2]}")
            
            id_avaliacao = input("ID da avaliação de prova: ")
            id_juiz = input("ID do juiz: ")
            nota_final = input("Nota final (0-10): ")

            query = "INSERT INTO avaliacao_avaliador (id_avaliacao, id_juiz, nota_final) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (id_avaliacao, id_juiz, nota_final))
            self.connection.commit()
            print("Avaliação do avaliador inserida com sucesso!")
            
        except Error as e:
            print(f"Erro ao inserir avaliação do avaliador: {e}")

    def inserir_avaliacao_criterio(self):
        try:
            print("\n--- INSERIR AVALIAÇÃO DE CRITÉRIO ---")
            
            # Listar avaliações de avaliador disponíveis
            print("\nAvaliações de avaliador disponíveis:")
            query_avaliadores = """
            SELECT aa.id_avaliador_prova, e.nome_equipe, p.nome_primeiro, p.nome_ultimo, aa.nota_final
            FROM avaliacao_avaliador aa
            JOIN avaliacao_prova ap ON aa.id_avaliacao = ap.id_avaliacao
            JOIN equipe e ON ap.id_equipe = e.id_equipe
            JOIN juiz j ON aa.id_juiz = j.id_pessoa
            JOIN pessoa p ON j.id_pessoa = p.id_pessoa
            """
            self.cursor.execute(query_avaliadores)
            avaliadores = self.cursor.fetchall()
            for av in avaliadores:
                print(f"ID: {av[0]} | Equipe: {av[1]} | Juiz: {av[2]} {av[3]} | Nota: {av[4]}")
            
            # Listar critérios disponíveis
            print("\nCritérios de avaliação disponíveis:")
            query_criterios = "SELECT id_criterio, nome_criterio, pontuacao_maxima FROM criterio"
            self.cursor.execute(query_criterios)
            criterios = self.cursor.fetchall()
            for crit in criterios:
                print(f"ID: {crit[0]} | Critério: {crit[1]} | Pontuação Máxima: {crit[2]}")
            
            id_avaliador_prova = input("ID da avaliação do avaliador: ")
            id_criterio = input("ID do critério: ")
            nota_criterio = input("Nota do critério (0-10): ")

            query = "INSERT INTO avaliacao_criterio (id_avaliador_prova, id_criterio, nota_criterio) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (id_avaliador_prova, id_criterio, nota_criterio))
            self.connection.commit()
            print("Avaliação de critério inserida com sucesso!")
            
        except Error as e:
            print(f"Erro ao inserir avaliação de critério: {e}")

    def inserir_patrocina(self):
        try:
            print("\n--- INSERIR PATROCÍNIO ---")
            self.listar_patrocinadores()
            self.listar_equipes()
            id_patrocinador = input("ID do patrocinador: ")
            id_equipe = input("ID da equipe: ")
            valor_total = input("Valor total: ")
            data_inicio = input("Data de início (YYYY-MM-DD): ")

            query = "INSERT INTO patrocina (id_patrocinador, id_equipe, valor_total, data_inicio) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (id_patrocinador, id_equipe, valor_total, data_inicio))
            self.connection.commit()
            print("Patrocínio inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir patrocínio: {e}")

    def inserir_possui(self):
        try:
            print("\n--- INSERIR INGREDIENTE NA PROVA ---")
            
            # Listar provas disponíveis
            print("\nProvas disponíveis:")
            query_provas = """
            SELECT id_prova, descricao_prova, dificuldade, tempo 
            FROM prova
            """
            self.cursor.execute(query_provas)
            provas = self.cursor.fetchall()
            for prova in provas:
                print(f"ID: {prova[0]} | Descrição: {prova[1]} | Dificuldade: {prova[2]} | Tempo: {prova[3]}")
            
            # Listar ingredientes disponíveis
            print("\nIngredientes disponíveis:")
            query_ingredientes = """
            SELECT i.id_ingrediente, i.nome_ingrediente, 
                COALESCE(p.nome_patrocinador, 'Sem patrocinador') as patrocinador,
                CASE 
                    WHEN cc.id_ingrediente IS NOT NULL THEN 'Corte de Carne'
                    ELSE 'Outro Ingrediente'
                END as tipo
            FROM ingrediente i
            LEFT JOIN patrocinador p ON i.id_patrocinador = p.id_patrocinador
            LEFT JOIN corte_carne cc ON i.id_ingrediente = cc.id_ingrediente
            """
            self.cursor.execute(query_ingredientes)
            ingredientes = self.cursor.fetchall()
            for ing in ingredientes:
                print(f"ID: {ing[0]} | Nome: {ing[1]} | Patrocinador: {ing[2]} | Tipo: {ing[3]}")
            
            id_prova = input("ID da prova: ")
            id_ingrediente = input("ID do ingrediente: ")

            query = "INSERT INTO possui (id_prova, id_ingrediente) VALUES (%s, %s)"
            self.cursor.execute(query, (id_prova, id_ingrediente))
            self.connection.commit()
            print("Ingrediente associado à prova com sucesso!")
            
        except Error as e:
            print(f"Erro ao associar ingrediente à prova: {e}")

    # MÉTODOS PARA LISTAR DADOS
    def listar_paises(self):
        try:
            self.cursor.execute("SELECT * FROM pais")
            paises = self.cursor.fetchall()

            print("\n--- LISTA DE PAÍSES ---")
            for pais in paises:
                print(f"ID: {pais[0]}, Nome: {pais[1]}")
        except Error as e:
            print(f"Erro ao listar países: {e}")

    def listar_equipes(self):
        try:
            query = """
            SELECT e.id_equipe, e.nome_equipe, p.nome_pais 
            FROM equipe e 
            JOIN pais p ON e.id_pais = p.id_pais
            """
            self.cursor.execute(query)
            equipes = self.cursor.fetchall()

            print("\n--- LISTA DE EQUIPES ---")
            for equipe in equipes:
                print(f"ID: {equipe[0]}, Nome: {equipe[1]}, País: {equipe[2]}")
        except Error as e:
            print(f"Erro ao listar equipes: {e}")

    def listar_patrocinadores(self):
        try:
            self.cursor.execute("SELECT * FROM patrocinador")
            patrocinadores = self.cursor.fetchall()

            print("\n--- LISTA DE PATROCINADORES ---")
            for pat in patrocinadores:
                print(f"ID: {pat[0]}, Nome: {pat[1]}, Descrição: {pat[2]}")
        except Error as e:
            print(f"Erro ao listar patrocinadores: {e}")

    def listar_pessoas(self):
        try:
            self.cursor.execute("SELECT * FROM pessoa")
            pessoas = self.cursor.fetchall()

            print("\n--- LISTA DE PESSOAS ---")
            for pessoa in pessoas:
                if pessoa[5] == 1:
                    tipo = "Juiz"
                else:
                    tipo = "Competidor"
                print(f"ID: {pessoa[0]}, Nome: {pessoa[1]} {pessoa[2]}, Telefone: {pessoa[3]}, Nascimento: {pessoa[4]}, Tipo: {tipo}")
        except Error as e:
            print(f"Erro ao listar pessoas: {e}")

    def listar_pessoas_juizes(self):
        try:
            self.cursor.execute("SELECT * FROM pessoa WHERE tipo = 1")
            pessoas = self.cursor.fetchall()

            print("\n--- PESSOAS DO TIPO JUÍZ ---")
            for pessoa in pessoas:
                print(f"ID: {pessoa[0]}, Nome: {pessoa[1]} {pessoa[2]}")
        except Error as e:
            print(f"Erro ao listar pessoas juízes: {e}")

    def listar_pessoas_competidores(self):
        try:
            self.cursor.execute("SELECT * FROM pessoa WHERE tipo = 2")
            pessoas = self.cursor.fetchall()

            print("\n--- PESSOAS DO TIPO COMPETIDOR ---")
            for pessoa in pessoas:
                print(f"ID: {pessoa[0]}, Nome: {pessoa[1]} {pessoa[2]}")
        except Error as e:
            print(f"Erro ao listar pessoas competidores: {e}")

    def listar_juizes(self):
        try:
            query = """
            SELECT j.id_pessoa, p.nome_primeiro, p.nome_ultimo, j.data_admissao, j.descricao_juiz
            FROM juiz j 
            JOIN pessoa p ON j.id_pessoa = p.id_pessoa
            """
            self.cursor.execute(query)
            juizes = self.cursor.fetchall()

            print("\n--- LISTA DE JUÍZES ---")
            for juiz in juizes:
                print(f"ID Pessoa: {juiz[0]}, Nome: {juiz[1]} {juiz[2]}, Admissão: {juiz[3]}, Descrição: {juiz[4]}")
        except Error as e:
            print(f"Erro ao listar juízes: {e}")

    def listar_competidores(self):
        try:
            query = """
            SELECT c.id_pessoa, p.nome_primeiro, p.nome_ultimo, c.data_inscricao, e.nome_equipe
            FROM competidor c 
            JOIN pessoa p ON c.id_pessoa = p.id_pessoa
            JOIN equipe e ON c.id_equipe = e.id_equipe
            """
            self.cursor.execute(query)
            competidores = self.cursor.fetchall()

            print("\n--- LISTA DE COMPETIDORES ---")
            for comp in competidores:
                print(f"ID Pessoa: {comp[0]}, Nome: {comp[1]} {comp[2]}, Inscrição: {comp[3]}, Equipe: {comp[4]}")
        except Error as e:
            print(f"Erro ao listar competidores: {e}")

    def listar_provas(self):
        try:
            self.cursor.execute("SELECT * FROM prova")
            provas = self.cursor.fetchall()

            print("\n--- LISTA DE PROVAS ---")
            for prova in provas:
                print(f"ID: {prova[0]}, Tempo: {prova[1]}, Dificuldade: {prova[2]}, Descrição: {prova[3]}")
        except Error as e:
            print(f"Erro ao listar provas: {e}")

    def listar_ingredientes(self):
        try:
            query = """
            SELECT i.id_ingrediente, i.nome_ingrediente, p.nome_patrocinador
            FROM ingrediente i 
            LEFT JOIN patrocinador p ON i.id_patrocinador = p.id_patrocinador
            """
            self.cursor.execute(query)
            ingredientes = self.cursor.fetchall()

            print("\n--- LISTA DE INGREDIENTES ---")
            for ing in ingredientes:
                patrocinador = ing[2] if ing[2] else "Nenhum"
                print(f"ID: {ing[0]}, Nome: {ing[1]}, Patrocinador: {patrocinador}")
        except Error as e:
            print(f"Erro ao listar ingredientes: {e}")

    def listar_cortes_carne(self):
        try:
            query = """
            SELECT cc.id_ingrediente, i.nome_ingrediente, cc.tipo, cc.descricao
            FROM corte_carne cc 
            JOIN ingrediente i ON cc.id_ingrediente = i.id_ingrediente
            """
            self.cursor.execute(query)
            cortes = self.cursor.fetchall()

            print("\n--- LISTA DE CORTES DE CARNE ---")
            for corte in cortes:
                tipo_desc = {1: "Bovina", 2: "Suína", 3: "Frango", 4: "Outros"}
                print(f"ID Ingrediente: {corte[0]}, Nome: {corte[1]}, Tipo: {tipo_desc.get(corte[2], 'Desconhecido')}, Descrição: {corte[3]}")
        except Error as e:
            print(f"Erro ao listar cortes de carne: {e}")

    def listar_criterios(self):
        try:
            self.cursor.execute("SELECT * FROM criterio")
            criterios = self.cursor.fetchall()

            print("\n--- LISTA DE CRITÉRIOS ---")
            for crit in criterios:
                print(f"ID: {crit[0]}, Nome: {crit[1]}, Descrição: {crit[2]}, Pontuação Máxima: {crit[3]}")
        except Error as e:
            print(f"Erro ao listar critérios: {e}")

    def listar_avaliacoes_prova(self):
        try:
            query = """
            SELECT ap.id_avaliacao, e.nome_equipe, ap.data
            FROM avaliacao_prova ap 
            JOIN equipe e ON ap.id_equipe = e.id_equipe
            """
            self.cursor.execute(query)
            avaliacoes = self.cursor.fetchall()
            
            print("\n--- LISTA DE AVALIAÇÕES DE PROVA ---")
            for aval in avaliacoes:
                print(f"ID: {aval[0]}, Equipe: {aval[1]}, Data: {aval[2]}")
        except Error as e:
            print(f"Erro ao listar avaliações de prova: {e}")

    def listar_avaliacoes_avaliador(self):
        try:
            query = """
            SELECT 
                aa.id_avaliador_prova,
                e.nome_equipe,
                p.nome_primeiro || ' ' || p.nome_ultimo AS nome_juiz,
                aa.nota_final,
                ap.data
            FROM avaliacao_avaliador aa
            JOIN avaliacao_prova ap ON aa.id_avaliacao = ap.id_avaliacao
            JOIN equipe e ON ap.id_equipe = e.id_equipe
            JOIN juiz j ON aa.id_juiz = j.id_pessoa
            JOIN pessoa p ON j.id_pessoa = p.id_pessoa
            """
            self.cursor.execute(query)
            avaliacoes = self.cursor.fetchall()
            
            print("\n--- LISTA DE AVALIAÇÕES DO AVALIADOR ---")
            for aval in avaliacoes:
                print(f"ID: {aval[0]}, Equipe: {aval[1]}, Juiz: {aval[2]}, Nota Final: {aval[3]}, Data: {aval[4]}")
        except Error as e:
            print(f"Erro ao listar avaliações do avaliador: {e}")

    def listar_avaliacoes_criterio(self):
        try:
            query = """
            SELECT 
                ac.id_avaliador_criterio,
                e.nome_equipe,
                p.nome_primeiro || ' ' || p.nome_ultimo AS nome_juiz,
                c.nome_criterio,
                ac.nota_criterio,
                c.pontuacao_maxima,
                ap.data
            FROM avaliacao_criterio ac
            JOIN avaliacao_avaliador aa ON ac.id_avaliador_prova = aa.id_avaliador_prova
            JOIN avaliacao_prova ap ON aa.id_avaliacao = ap.id_avaliacao
            JOIN equipe e ON ap.id_equipe = e.id_equipe
            JOIN juiz j ON aa.id_juiz = j.id_pessoa
            JOIN pessoa p ON j.id_pessoa = p.id_pessoa
            JOIN criterio c ON ac.id_criterio = c.id_criterio
            """
            self.cursor.execute(query)
            avaliacoes = self.cursor.fetchall()
            
            print("\n--- LISTA DE AVALIAÇÕES POR CRITÉRIO ---")
            for aval in avaliacoes:
                print(f"ID: {aval[0]}, Equipe: {aval[1]}, Juiz: {aval[2]}, Critério: {aval[3]}, Nota: {aval[4]}/{aval[5]}, Data: {aval[6]}")
        except Error as e:
            print(f"Erro ao listar avaliações por critério: {e}")

    def listar_patrocina(self):
        try:
            query = """
            SELECT pat.nome_patrocinador, eq.nome_equipe, p.valor_total, p.data_inicio
            FROM patrocina p 
            JOIN patrocinador pat ON p.id_patrocinador = pat.id_patrocinador
            JOIN equipe eq ON p.id_equipe = eq.id_equipe
            """
            self.cursor.execute(query)
            patrocinios = self.cursor.fetchall()
            
            print("\n--- LISTA DE PATROCÍNIOS ---")
            for pat in patrocinios:
                print(f"Patrocinador: {pat[0]}, Equipe: {pat[1]}, Valor: R${pat[2]}, Início: {pat[3]}")
        except Error as e:
            print(f"Erro ao listar patrocínios: {e}")

    def listar_possui(self):
        try:
            query = """
            SELECT 
                pr.id_prova,
                pr.descricao_prova,
                pr.dificuldade,
                pr.tempo,
                i.id_ingrediente,
                i.nome_ingrediente,
                COALESCE(p.nome_patrocinador, 'Sem patrocinador') as patrocinador,
                CASE 
                    WHEN cc.id_ingrediente IS NOT NULL THEN 'Corte de Carne'
                    ELSE 'Outro Ingrediente'
                END as tipo_ingrediente
            FROM possui po
            JOIN prova pr ON po.id_prova = pr.id_prova
            JOIN ingrediente i ON po.id_ingrediente = i.id_ingrediente
            LEFT JOIN patrocinador p ON i.id_patrocinador = p.id_patrocinador
            LEFT JOIN corte_carne cc ON i.id_ingrediente = cc.id_ingrediente
            ORDER BY pr.id_prova, i.id_ingrediente
            """
            self.cursor.execute(query)
            associacoes = self.cursor.fetchall()
            
            print("\n--- LISTA DE INGREDIENTES POR PROVA ---")
            for assoc in associacoes:
                print(f"Prova ID: {assoc[0]} | Descrição: {assoc[1]} | Dificuldade: {assoc[2]} | Tempo: {assoc[3]}")
                print(f"  └── Ingrediente ID: {assoc[4]} | Nome: {assoc[5]} | Patrocinador: {assoc[6]} | Tipo: {assoc[7]}")
                print()
        except Error as e:
            print(f"Erro ao listar ingredientes por prova: {e}")


    # MÉTODOS PARA ATUALIZAR DADOS
    def atualizar_equipe(self):
        try:
            self.listar_equipes()
            id_equipe = input("\nID da equipe a ser atualizada: ")
            nome_equipe = input("Novo nome da equipe: ")
            self.listar_paises()
            id_pais = input("Novo ID do país: ")
            
            query = "UPDATE equipe SET nome_equipe = %s, id_pais = %s WHERE id_equipe = %s"
            self.cursor.execute(query, (nome_equipe, id_pais, id_equipe))
            self.connection.commit()
            print("Equipe atualizada com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar equipe: {e}")

    def atualizar_pessoa(self):
        try:
            self.listar_pessoas()
            id_pessoa = input("\nID da pessoa a ser atualizada: ")
            nome_primeiro = input("Novo primeiro nome: ")
            nome_ultimo = input("Novo último nome: ")
            numero_telefone = input("Novo telefone: ")
            data_nascimento = input("Nova data de nascimento (YYYY-MM-DD): ")
            
            query = "UPDATE pessoa SET nome_primeiro = %s, nome_ultimo = %s, numero_telefone = %s, data_nascimento = %s WHERE id_pessoa = %s"
            self.cursor.execute(query, (nome_primeiro, nome_ultimo, numero_telefone, data_nascimento, id_pessoa))
            self.connection.commit()
            print("Pessoa atualizada com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar pessoa: {e}")

    def atualizar_patrocinador(self):
        try:
            self.listar_patrocinadores()
            id_patrocinador = input("\nID do patrocinador a ser atualizado: ")
            nome_patrocinador = input("Novo nome: ")
            descricao_patrocinador = input("Nova descrição: ")
            
            query = "UPDATE patrocinador SET nome_patrocinador = %s, descricao_patrocinador = %s WHERE id_patrocinador = %s"
            self.cursor.execute(query, (nome_patrocinador, descricao_patrocinador, id_patrocinador))
            self.connection.commit()
            print("Patrocinador atualizado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar patrocinador: {e}")

    def atualizar_prova(self):
        try:
            self.listar_provas()
            id_prova = input("\nID da prova a ser atualizada: ")
            tempo = input("Novo tempo (HH:MM): ")
            dificuldade = input("Nova dificuldade (1-3): ")
            descricao_prova = input("Nova descrição: ")
            
            query = "UPDATE prova SET tempo = %s, dificuldade = %s, descricao_prova = %s WHERE id_prova = %s"
            self.cursor.execute(query, (tempo, dificuldade, descricao_prova, id_prova))
            self.connection.commit()
            print("Prova atualizada com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar prova: {e}")

    # MÉTODOS PARA REMOVER DADOS
    def remover_pais(self):
        try:
            self.listar_paises()
            id_pais = input("\nID do país a ser removido: ")

            query = "DELETE FROM pais WHERE id_pais = %s"
            self.cursor.execute(query, (id_pais,))
            self.connection.commit()

            print("País removido com sucesso!")
            print("\nLista atualizada:")
            self.listar_paises()

        except Error as e:
            print(f"Erro ao remover país: {e}")
    
    def remover_equipe(self):
        try:
            self.listar_equipes()
            id_equipe = input("\nID da equipe a ser removida: ")
            
            query = "DELETE FROM equipe WHERE id_equipe = %s"
            self.cursor.execute(query, (id_equipe,))
            self.connection.commit()
            self.listar_equipes()
            print("Equipe removida com sucesso!")
        except Error as e:
            print(f"Erro ao remover equipe: {e}")

    def remover_pessoa(self):
        try:
            self.listar_pessoas()
            id_pessoa = input("\nID da pessoa a ser removida: ")
            
            query = "DELETE FROM pessoa WHERE id_pessoa = %s"
            self.cursor.execute(query, (id_pessoa,))
            self.connection.commit()
            self.listar_pessoas()
            print("Pessoa removida com sucesso!")
        except Error as e:
            print(f"Erro ao remover pessoa: {e}")

    def remover_patrocinador(self):
        try:
            self.listar_patrocinadores()
            id_patrocinador = input("\nID do patrocinador a ser removido: ")
            
            query = "DELETE FROM patrocinador WHERE id_patrocinador = %s"
            self.cursor.execute(query, (id_patrocinador,))
            self.connection.commit()
            self.listar_patrocinadores()
            print("Patrocinador removido com sucesso!")
        except Error as e:
            print(f"Erro ao remover patrocinador: {e}")

    def remover_juiz(self):
        try:
            self.listar_juizes() 
            id_pessoa = input("\nID da pessoa (juiz) a ser removida: ")

            query = "DELETE FROM juiz WHERE id_pessoa = %s"
            self.cursor.execute(query, (id_pessoa,))
            self.connection.commit()

            print("Juiz removido com sucesso!")
            print("\nLista atualizada:")
            self.listar_juizes()

        except Error as e:
            print(f"Erro ao remover juiz: {e}")
            
    def remover_competidor(self):
        try:
            self.listar_competidores()
            id_patrocinador = input("\nID da pessoa (competidora) a ser removida: ")
            
            query = "DELETE FROM competidor WHERE id_pessoa = %s"
            self.cursor.execute(query, (id_patrocinador,))
            self.connection.commit()
            self.listar_competidores()
            print("Competidor removido com sucesso!")
        except Error as e:
            print(f"Erro ao remover o competidor: {e}")
            
    def remover_ingrediente(self):
        try:
            self.listar_ingredientes()
            id_ingrediente = input("\nID do ingrediente a ser removido: ")
            
            query = "DELETE FROM ingrediente WHERE id_ingrediente = %s"
            self.cursor.execute(query, (id_ingrediente,))
            self.connection.commit()
            self.listar_ingredientes()
            print("Ingrediente removido com sucesso!")
        except Error as e:
            print(f"Erro ao remover ingrediente: {e}")
            
    def remover_cortes_carne(self):
        try:
            self.listar_cortes_carne() 
            id_corte = input("\nID do corte de carne a ser removido: ")
            query = """
                DELETE FROM corte_carne
                WHERE id_ingrediente = %s
            """
            self.cursor.execute(query, (id_corte,))
            self.connection.commit()
            print("\nCorte de carne removido com sucesso!")
            print("\nLista atualizada:")
            self.listar_cortes_carne()

        except Error as e:
            print(f"Erro ao remover corte de carne: {e}")

    def remover_criterio(self):
        try:
            self.listar_criterios() 
            id_criterio = input("\nID do critério a ser removido: ")

            query = "DELETE FROM criterio WHERE id_criterio = %s"
            self.cursor.execute(query, (id_criterio,))
            self.connection.commit()

            print("\nCritério removido com sucesso!")
            print("\nLista atualizada:")
            self.listar_criterios()

        except Error as e:
            print(f"Erro ao remover critério: {e}")

    def remover_avaliacao_prova(self):
        try:
            self.listar_avaliacoes_prova()  # lista as avaliações cadastradas
            id_avaliacao = input("\nID da avaliação de prova a ser removida: ")

            query = "DELETE FROM avaliacao_prova WHERE id_avaliacao = %s"
            self.cursor.execute(query, (id_avaliacao,))
            self.connection.commit()

            print("\nAvaliação de prova removida com sucesso!")
            print("\nLista atualizada:")
            self.listar_avaliacoes_prova()

        except Error as e:
            print(f"Erro ao remover avaliação de prova: {e}")

    def remover_prova(self):
        try:
            self.listar_provas()
            id_prova = input("\nID da prova a ser removida: ")
            
            query = "DELETE FROM prova WHERE id_prova = %s"
            self.cursor.execute(query, (id_prova,))
            self.connection.commit()
            print("Prova removida com sucesso!")
        except Error as e:
            print(f"Erro ao remover prova: {e}")

    def remover_patrocina(self):
        try:
            self.listar_patrocina()
            self.listar_patrocinadores()
            patrocinador = input("\nID do patrocinador que será excluido o patrocínio: ")
            self.listar_equipes()
            equipe = input("\nID da equipe que vai ser excluido o patrocínio: ")
            
            query = """
            DELETE FROM patrocina 
            WHERE id_patrocinador = (SELECT id_patrocinador FROM patrocinador WHERE id_patrocinador = %s)
            AND id_equipe = (SELECT id_equipe FROM equipe WHERE id_equipe = %s)
            """
            self.cursor.execute(query, (patrocinador, equipe))
            self.connection.commit()
            self.listar_patrocina()
            print("Patrocínio removido com sucesso!")
        except Error as e:
            print(f"Erro ao remover patrocínio: {e}")

    def remover_avaliacao_avaliador(self):
        try:
            self.listar_avaliacoes_avaliador()  # lista as avaliações de avaliador cadastradas
            id_avaliador_prova = input("\nID da avaliação do avaliador a ser removida: ")

            # Primeiro verificar se existem critérios associados
            query_check = """
            SELECT COUNT(*) FROM avaliacao_criterio 
            WHERE id_avaliador_prova = %s
            """
            self.cursor.execute(query_check, (id_avaliador_prova,))
            count = self.cursor.fetchone()[0]
            
            if count > 0:
                print(f"\nATENÇÃO: Esta avaliação possui {count} critério(s) associado(s).")
                confirm = input("Deseja remover mesmo assim? (s/N): ")
                if confirm.lower() != 's':
                    print("Remoção cancelada.")
                    return

            query = "DELETE FROM avaliacao_avaliador WHERE id_avaliador_prova = %s"
            self.cursor.execute(query, (id_avaliador_prova,))
            self.connection.commit()

            print("\nAvaliação do avaliador removida com sucesso!")
            print("\nLista atualizada:")
            self.listar_avaliacoes_avaliador()

        except Error as e:
            print(f"Erro ao remover avaliação do avaliador: {e}")

    def remover_avaliacao_criterio(self):
        try:
            self.listar_avaliacoes_criterio()  # lista as avaliações de critério cadastradas
            id_avaliador_criterio = input("\nID da avaliação de critério a ser removida: ")

            query = "DELETE FROM avaliacao_criterio WHERE id_avaliador_criterio = %s"
            self.cursor.execute(query, (id_avaliador_criterio,))
            self.connection.commit()

            print("\nAvaliação de critério removida com sucesso!")
            print("\nLista atualizada:")
            self.listar_avaliacoes_criterio()

        except Error as e:
            print(f"Erro ao remover avaliação de critério: {e}")

    def remover_possui(self):
        try:
            self.listar_possui()  # lista as associações cadastradas
            
            id_prova = input("\nID da prova da associação a ser removida: ")
            id_ingrediente = input("ID do ingrediente da associação a ser removida: ")

            query = "DELETE FROM possui WHERE id_prova = %s AND id_ingrediente = %s"
            self.cursor.execute(query, (id_prova, id_ingrediente))
            self.connection.commit()

            print("\nAssociação removida com sucesso!")
            print("\nLista atualizada:")
            self.listar_possui()

        except Error as e:
            print(f"Erro ao remover associação: {e}")

    # CONSULTAS ESPECIAIS

    def consulta_pais_equipes_integrantes(self):
        try:
            print("\n--- PAÍSES, EQUIPES E SEUS INTEGRANTES ---")
            query = """
                SELECT 
                    pa.nome_pais,
                    e.nome_equipe,
                    COALESCE(p.nome_primeiro || ' ' || p.nome_ultimo, 'Sem competidor') AS nome_completo
                FROM pais pa
                JOIN equipe e ON pa.id_pais = e.id_pais
                LEFT JOIN competidor comp ON e.id_equipe = comp.id_equipe
                LEFT JOIN pessoa p ON comp.id_pessoa = p.id_pessoa
                ORDER BY pa.nome_pais, e.nome_equipe, nome_completo
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            pais_atual = None
            equipe_atual = None

            for linha in resultados:
                pais, equipe, competidor = linha
                if pais != pais_atual:
                    print(f"\nPaís: {pais}")
                    pais_atual = pais
                    equipe_atual = None
                if equipe != equipe_atual:
                    print(f"   Equipe: {equipe}")
                    equipe_atual = equipe
                print(f"      Integrante: {competidor}")

        except Error as e:
            print(f"Erro na consulta: {e}")
        
    def consulta_equipes_sem_competidores(self):
        try:
            print("\n--- EQUIPES SEM COMPETIDORES ---")
            query = """
                SELECT 
                    e.nome_equipe,
                    p.nome_pais
                FROM equipe e
                JOIN pais p ON e.id_pais = p.id_pais
                WHERE e.id_equipe NOT IN (
                    SELECT DISTINCT id_equipe 
                    FROM competidor 
                    WHERE id_equipe IS NOT NULL
                )
                ORDER BY p.nome_pais, e.nome_equipe
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            if not resultados:
                print("Todas as equipes têm competidores!")
                return

            pais_atual = None
            for linha in resultados:
                equipe, pais = linha
                if pais != pais_atual:
                    print(f"\nPaís: {pais}")
                    pais_atual = pais
                print(f"   Equipe: {equipe}")

        except Error as e:
            print(f"Erro na consulta: {e}")
            
    def consulta_ingredientes_nao_utilizados(self):
        try:
            print("\n--- INGREDIENTES NÃO UTILIZADOS EM PROVAS ---")
            query = """
                SELECT 
                    i.nome_ingrediente,
                    pat.nome_patrocinador
                FROM ingrediente i
                LEFT JOIN patrocinador pat ON i.id_patrocinador = pat.id_patrocinador
                WHERE i.id_ingrediente NOT IN (
                    SELECT DISTINCT id_ingrediente 
                    FROM possui 
                    WHERE id_ingrediente IS NOT NULL
                )
                ORDER BY i.nome_ingrediente
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            if not resultados:
                print("Todos os ingredientes são utilizados em provas!")
                return

            print(f"{'Ingrediente':<25} {'Patrocinador':<20}")
            print("-" * 50)
            for linha in resultados:
                ingrediente, patrocinador = linha
                patrocinador = patrocinador if patrocinador else "Nenhum"
                print(f"{ingrediente:<25} {patrocinador:<20}")

        except Error as e:
            print(f"Erro na consulta: {e}")

    def consulta_equipes_mais_competidores(self):
        try:
            print("\n--- EQUIPES COM MAIS COMPETIDORES ---")
            query = """
                SELECT 
                    e.nome_equipe,
                    p.nome_pais,
                    COUNT(comp.id_pessoa) AS total_competidores
                FROM equipe e
                JOIN pais p ON e.id_pais = p.id_pais
                LEFT JOIN competidor comp ON e.id_equipe = comp.id_equipe
                GROUP BY e.id_equipe, e.nome_equipe, p.nome_pais
                HAVING COUNT(comp.id_pessoa) > 0
                ORDER BY total_competidores DESC, e.nome_equipe
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            print(f"{'Equipe':<20} {'País':<15} {'Total Competidores':<20}")
            print("-" * 60)
            for linha in resultados:
                equipe, pais, total = linha
                print(f"{equipe:<20} {pais:<15} {total:<20}")

        except Error as e:
            print(f"Erro na consulta: {e}")

    def consulta_media_notas_juiz(self):
        try:
            print("\n--- MÉDIA DE NOTAS POR JUIZ ---")
            query = """
                SELECT 
                    p.nome_primeiro || ' ' || p.nome_ultimo AS nome_juiz,
                    COUNT(aa.id_avaliador_prova) AS total_avaliacoes,
                    ROUND(AVG(aa.nota_final), 2) AS media_notas,
                    MIN(aa.nota_final) AS nota_minima,
                    MAX(aa.nota_final) AS nota_maxima
                FROM juiz j
                JOIN pessoa p ON j.id_pessoa = p.id_pessoa
                JOIN avaliacao_avaliador aa ON j.id_pessoa = aa.id_juiz
                GROUP BY j.id_pessoa, p.nome_primeiro, p.nome_ultimo
                HAVING COUNT(aa.id_avaliador_prova) > 0
                ORDER BY media_notas DESC
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            print(f"{'Juiz':<25} {'Avaliações':<12} {'Média':<8} {'Mínima':<8} {'Máxima':<8}")
            print("-" * 65)
            for linha in resultados:
                juiz, total, media, minima, maxima = linha
                print(f"{juiz:<25} {total:<12} {media:<8} {minima:<8} {maxima:<8}")

        except Error as e:
            print(f"Erro na consulta: {e}")

    def consulta_diferenca_provas_ingredientes(self):
        try:
            print("\n--- DIFERENÇA: PROVAS COM E SEM INGREDIENTES ESPECÍFICOS ---")
            print("Mostra provas que usam ingredientes patrocinados, mas NAO usam cortes de carne")
            
            query = """
                -- Provas que usam ingredientes patrocinados
                SELECT DISTINCT pr.id_prova, pr.descricao_prova, pr.dificuldade
                FROM prova pr
                JOIN possui po ON pr.id_prova = po.id_prova
                JOIN ingrediente i ON po.id_ingrediente = i.id_ingrediente
                WHERE i.id_patrocinador IS NOT NULL
                
                EXCEPT

                -- Provas que usam cortes de carne
                SELECT DISTINCT pr.id_prova, pr.descricao_prova, pr.dificuldade
                FROM prova pr
                JOIN possui po ON pr.id_prova = po.id_prova
                JOIN corte_carne cc ON po.id_ingrediente = cc.id_ingrediente
                ORDER BY dificuldade, descricao_prova
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            if not resultados:
                print("Nao ha provas que atendam a esses criterios!")
                return

            print("Provas que usam ingredientes patrocinados, mas NAO usam cortes de carne:")
            print(f"{'ID':<8} {'Descricao':<40} {'Dificuldade':<12}")
            print("-" * 65)
            for linha in resultados:
                id_prova, descricao, dificuldade = linha
                nivel = {1: "Facil", 2: "Medio", 3: "Dificil"}
                print(f"{id_prova:<8} {descricao:<40} {nivel.get(dificuldade, 'N/A'):<12}")

        except Error as e:
            print(f"Erro na consulta: {e}")

    def consulta_uniao_patrocinadores_ingredientes(self):
        try:
            print("\n--- UNIAO: PATROCINADORES E SEUS INGREDIENTES ---")
            print("Lista unificada de patrocinadores e ingredientes patrocinados")
            
            query = """
                -- Todos os patrocinadores (mesmo os sem ingredientes)
                SELECT 
                    'PATROCINADOR' AS tipo,
                    id_patrocinador AS id,
                    nome_patrocinador AS nome,
                    descricao_patrocinador AS descricao,
                    NULL AS patrocinador_associado
                FROM patrocinador

                UNION ALL

                -- Todos os ingredientes patrocinados
                SELECT 
                    'INGREDIENTE' AS tipo,
                    i.id_ingrediente AS id,
                    i.nome_ingrediente AS nome,
                    NULL AS descricao,
                    p.nome_patrocinador AS patrocinador_associado
                FROM ingrediente i
                JOIN patrocinador p ON i.id_patrocinador = p.id_patrocinador
                WHERE i.id_patrocinador IS NOT NULL

                ORDER BY tipo DESC, patrocinador_associado, nome
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()

            print("Lista completa de patrocinadores e ingredientes patrocinados:")
            print("-" * 80)
            
            patrocinador_atual = None
            for linha in resultados:
                tipo, id_item, nome, descricao, patrocinador_assoc = linha
                
                if tipo == "PATROCINADOR":
                    print(f"\nPATROCINADOR: {nome}")
                    if descricao:
                        print(f"   Descricao: {descricao}")
                    patrocinador_atual = nome
                else:  # INGREDIENTE
                    if patrocinador_assoc != patrocinador_atual:
                        print(f"\nIngredientes de {patrocinador_assoc}:")
                        patrocinador_atual = patrocinador_assoc
                    print(f"   - {nome}")

        except Error as e:
            print(f"Erro na consulta: {e}")

        # Função principal
def main():
    gerenciador = GerenciadorBanco()
    
    if gerenciador.conectar():
        gerenciador.menu_principal()
        gerenciador.desconectar()

if __name__ == "__main__":
    main()