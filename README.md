# 🍖🔥 Sistema de Gerenciamento de Campeonato Mundial de Churrasco

Este projeto implementa um sistema fictício de gestão para um campeonato mundial de churrasco. O sistema foi desenvolvido para organizar, automatizar e centralizar todas as informações e processos relacionados ao evento.

Este é um projeto de avaliação para a matéria **ACH2004 - Bancos de Dados I**, ministrada pela professora Fátima de Lourdes dos Santos Nunes Marques.

<div align="center">
  <img src="img/churra.png" alt="Churrasqueira com costela UHUMMM">
</div>

---

## ✔️ Requisitos

Para rodar este projeto, precisamos ter o seguinte instalado na sua máquina:

* **Python** (versão 3.10 ou superior)
* **PostgreSQL** (servidor de banco de dados)

---

## 🛠️ Como Utilizar

Seguir os passos abaixo para clonar o projeto, configurar o banco de dados e executar o sistema.

1.  **Clone o Repositório**
    Abra o terminal e clone o projeto usando o Git.
    ```bash
    git clone https://github.com/ka3ych/Campeonato_Mundial_de_Churrasco.git
    cd Campeonato_Mundial_de_Churrasco
    ```

2.  **Instale as Dependências**
    Instale as bibliotecas Python necessárias (como `customtkinter` e `psycopg2`). Para isso, crie um ambiente virtual (recomendado) e instale as dependências a partir do arquivo `requirements.txt`.
    ```bash
    # Crie e ative o ambiente virtual
    python -m venv venv
    # Para Windows:
    venv\Scripts\activate
    # Para macOS/Linux:
    source venv/bin/activate

    # Instale as dependências
    pip install -r requirements.txt
    ```

3.  **Configure e Crie o Banco de Dados**
    Certifique-se de que o seu servidor **PostgreSQL** está rodando. Em seguida, edite o arquivo `config.py` (se você tiver um, ou crie-o) com as suas credenciais de acesso ao PostgreSQL (user e senha conforme configurados na sua máquina)

    Após a configuração, execute o script de inicialização do banco de dados para criar as tabelas necessárias:
    ```bash
    python setup_database.py
    ```

4.  **Execute o Programa**
    Agora você pode iniciar a aplicação principal.
    ```bash
    python churras.py
    ```


   ---
   ## Referências
   - Conexão Python com o PostgreSQL:   [Link do vídeo no YouTube](https://youtu.be/tx5lmqBnArs?si=MwTL_P5bRNGN0oSj)
   - Documentação Oficial do CustomTkinter: [Link da documentação](https://customtkinter.tomschimansky.com/)  
   - GitHub com exemplos [Link](https://github.com/tomschimansky/customtkinter)  -> boa parte do deseign foi baseado nos exemplos deste repositório
