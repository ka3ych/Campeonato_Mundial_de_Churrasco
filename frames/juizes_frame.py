import customtkinter
import banco_excel
from datetime import datetime

class JuizFrame(customtkinter.CTkFrame):
    def __init__(self, parent, images):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1) # coluna para o painel lateral
        self.grid_rowconfigure(0, weight=1)

        self.div_principal = customtkinter.CTkFrame(self, fg_color="transparent")
        self.div_principal.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=(10, 20))

        self.div_principal.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)
        self.div_principal.grid_rowconfigure(3, weight=1)

        self.painel_lateral = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent", width=250)
        self.painel_lateral.grid(row=0, column=1, sticky="nsew", padx=(0, 20), pady=(100, 40))
        self.painel_lateral.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(
            self.div_principal, 
            text="Gerenciamento de Juízes",
            font=customtkinter.CTkFont(size=30, weight="bold")
        )
        self.title.grid(row=0, column=0, columnspan=4, padx=20, pady=(10, 20), sticky="w")

        # FRAME PARA OS FILTROS

        self.frame_filtros = customtkinter.CTkFrame(
            self.div_principal, 
            fg_color="transparent"
        )
        self.frame_filtros.grid(row=2, column=0, columnspan=9, padx=20, pady=0,sticky="nsew")
        self.frame_filtros.grid_columnconfigure((0,1,2,3,4,5,6, 7,8, 9, 10), weight=1)

        lista_paises = banco_excel.get_paises()
        lista_paises.insert(0, "Todos")
    
        self.filtro_pais = customtkinter.CTkOptionMenu(
            self.frame_filtros,
            dynamic_resizing=True,
            height=40,
            values=lista_paises,
            command=self.aplicar_filtro_pais
        )
        self.filtro_pais.set("Filtrar por país")
        self.filtro_pais.grid(row=0, column=0, padx=(0, 5), pady=(10,10), sticky="w")

        lista_cargos = banco_excel.get_cargos()
        lista_cargos.insert(0, "Todos")


        self.filtro_cargo = customtkinter.CTkOptionMenu(
            self.frame_filtros,
            dynamic_resizing=True,
            height=40,
            values=lista_cargos,
            command=self.aplica_filtro_cargo
        )
        self.filtro_cargo.set("Filtrar por cargo")
        self.filtro_cargo.grid(row=0, column=1, padx=(0,5), pady=(10,10), sticky="w")

        # FRAMES PARA OS PAINÉIS

        self.frame_analitico = customtkinter.CTkFrame(
            self.div_principal, 
            fg_color="transparent"
        )
        self.frame_analitico.grid(row=1, column=0, columnspan=12, padx=20, pady=(20, 40),sticky="nsew")
        self.frame_analitico.grid_columnconfigure((0,1,2), weight=1)

        # Total de juízes

        self.total_card = customtkinter.CTkFrame(
            self.frame_analitico, 
            fg_color="#00BF6E"
        )
        self.total_card.grid(row=0, column=0,  padx=(0, 20), sticky="nsew")
        customtkinter.CTkLabel(
            self.total_card, 
            text="Total de Juízes", 
            font=customtkinter.CTkFont(size=14)
        ).pack(padx=10, pady=5)
        
        self.total_label = customtkinter.CTkLabel(
            self.total_card, 
            text="...", 
            font=customtkinter.CTkFont(size=36, weight="bold")
        )
        self.total_label.pack(padx=10, pady=10) 

        self.atualizar_total_juiz()

        self.chart1_card = customtkinter.CTkFrame(
            self.frame_analitico, 
            fg_color="#AB00D1"
        )
        self.chart1_card.grid(row=0, column=1, padx=(0, 20), sticky="nsew")

        customtkinter.CTkLabel(
            self.chart1_card, 
            text="Países representados",
            font=customtkinter.CTkFont(size=14)
        ).pack(padx=10, pady=5)

        self.paises_label = customtkinter.CTkLabel(
            self.chart1_card, 
            text="...", 
            font=customtkinter.CTkFont(size=36, weight="bold")
        )
        self.paises_label.pack(padx=10, pady=10) 

        # Placeholder para Gráfico 2 (Juízes por Cargo) -> ARRUMAR
        self.chart2_card = customtkinter.CTkFrame(
            self.frame_analitico, 
            fg_color="#00B9D1"
        )
        self.chart2_card.grid(row=0, column=2, sticky="nsew")

        customtkinter.CTkLabel(
            self.chart2_card, 
            text="Mestres Churrasqueiros",
            font=customtkinter.CTkFont(size=14)
        ).pack(padx=10, pady=5)

        self.mestres_label = customtkinter.CTkLabel(
            self.chart2_card, 
            text="...", 
            font=customtkinter.CTkFont(size=36, weight="bold")
        )
        self.mestres_label.pack(padx=10, pady=10) 

        self.atualiza_metricas()


        # FRAME PARA A TABELA
        self.table_frame = customtkinter.CTkScrollableFrame(
            self.div_principal, 
            corner_radius=0,
            height=250
        )
        
        self.table_frame.grid(row=3, column=0, columnspan=12, padx=20, pady=(10, 20), sticky="nsew")

        self.desenhar_tabela()

        # ELEMENTOS DO PAINEL LATERAL PARA CADASTRO DE UM NOVO JUIZ
        form_title = customtkinter.CTkLabel(
            self.painel_lateral,
            text="Adicionar Novo Juiz",
            font=customtkinter.CTkFont(size=16, weight="bold")
        )
        form_title.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

        campos = [
            ("Nome", "Digite o nome completo", "entry"),
            ("País", "Selecione o país", "dropdown", ["Brasil", "Espanha", "Estados Unidos", "China", "Argentina"]),
            ("Cargo", "Selecione o cargo", "dropdown", ["Chef Executivo", "Mestre Churrasqueiro", "Crítica Gastronômica", "Jogador de algo"]),
            ("Telefone", "(00) 00000-0000", "entry"),
            ("Data de Nascimento", "dd/mm/aaaa", "entry")
        ]

        self.image_label = customtkinter.CTkLabel(
            self.painel_lateral, 
            text="", 
            image=images["jurado"])
        self.image_label.grid(row=0, column=0, padx=5, pady=0)

        self.form_entries = {}

        for i, (label_text, placeholder, tipo, *opcoes) in enumerate(campos):
            label = customtkinter.CTkLabel(
                self.painel_lateral, 
                text=label_text
            )
            label.grid(row=2*i + 2, column=0, padx=20, pady=(5,0), sticky="w")

            if tipo == "dropdown":
                entrada = customtkinter.CTkOptionMenu(
                    self.painel_lateral,
                    values=opcoes[0],
                    height=30
                )
            else:
                entrada = customtkinter.CTkEntry(
                    self.painel_lateral,
                    placeholder_text=placeholder,
                    height=30
                )
            entrada.grid(row=2*i + 3, column=0, padx=20, pady=5, sticky="ew")
            self.form_entries[label_text.lower().replace(" ", "_")] = entrada

            # Botão de Adicionar
            self.salvar_button = customtkinter.CTkButton(
                self.painel_lateral, 
                text="Salvar Juiz", 
                fg_color="#00BF6E", 
                height=30,
                command=self.salvar_juiz
            )
            self.salvar_button.grid(row=len(campos)*2 + 4, column=0, padx=20, pady=(20, 10), sticky="ew")

            # Botão de Limpar/Cancelar
            self.limpar_button = customtkinter.CTkButton(
                self.painel_lateral, 
                text="Limpar Campos", 
                fg_color="#3EB599",
                height=30,
                command=self.limpar_juiz
            )
            self.limpar_button.grid(row=len(campos)*2 + 5, column=0, padx=20, pady=(0, 20), sticky="ew")

    def atualizar_total_juiz(self):
        qtd_juiz = banco_excel.get_total_juizes()
        self.total_label.configure(text=str(qtd_juiz))

    def atualiza_metricas(self):
        total_paises = banco_excel.get_total_paises()
        self.paises_label.configure(text=str(total_paises))

        total_mestres = banco_excel.get_total_mestres()
        self.mestres_label.configure(text=str(total_mestres))

    def salvar_juiz(self):

        nome = self.form_entries['nome'].get()
        pais_origem = self.form_entries['país'].get()
        cargo = self.form_entries['cargo'].get()
        telefone = self.form_entries['telefone'].get()
        data_nascimento_str = self.form_entries['data_de_nascimento'].get()

        if not nome or pais_origem == "Selecione o país" or cargo == "Selecione o cargo":
                print("ERRO: Nome, País e Cargo são obrigatórios.")
                return
        data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()

        data_inicio = datetime.now().date()

        banco_excel.inserir_juiz(nome, pais_origem, cargo, telefone, data_nascimento, data_inicio)

        self.limpar_juiz()
        self.desenhar_tabela()
        self.atualizar_total_juiz()
        self.atualiza_metricas()
    
    def aplica_filtro_cargo(self, cargo):
        self.desenhar_tabela(filtro_cargo=cargo)
    
    def aplicar_filtro_pais(self, pais):
        self.desenhar_tabela(filtro_pais=pais)

    # Dentro da classe JuizFrame:
    def desenhar_tabela(self, filtro_pais=None, filtro_cargo=None):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        dados = banco_excel.get_juizes(filtro_pais=filtro_pais, filtro_cargo=filtro_cargo)
        
        headers = ["ID_Juiz", "Nome", "País", "Cargo", "Data de Admissão"]
        for col, header in enumerate(headers):
            header_label = customtkinter.CTkLabel(
                self.table_frame, 
                text=header, 
                font=customtkinter.CTkFont(weight="bold")
            )
            header_label.grid(row=0, column=col, padx=10, pady=5, sticky="w")
            self.table_frame.grid_columnconfigure(col, weight=1)

        for i, (id, nome, pais, cargo, data) in enumerate(dados):
            row = i + 1
            data_formatada = data.strftime('%d/%m/%Y')
            juiz_id = id # O ID é crucial para a exclusão

            # Colunas de dados
            customtkinter.CTkLabel(self.table_frame, text=id).grid(row=row, column=0, padx=10, pady=5)
            customtkinter.CTkLabel(self.table_frame, text=nome).grid(row=row, column=1, padx=10, pady=5)
            customtkinter.CTkLabel(self.table_frame, text=pais).grid(row=row, column=2, padx=10, pady=5)
            customtkinter.CTkLabel(self.table_frame, text=cargo).grid(row=row, column=3, padx=10, pady=5)
            customtkinter.CTkLabel(self.table_frame, text=data_formatada).grid(row=row, column=4, padx=10, pady=5)

            # Botões de Ação
            customtkinter.CTkButton(
                self.table_frame, 
                text="Editar", 
                width=60, 
                fg_color="#00BF6E", 
                state="disabled"
            ).grid(row=row, column=5, padx=5, pady=5)

            customtkinter.CTkButton(
                self.table_frame, 
                text="Excluir", 
                width=60, 
                fg_color="#E30000", 
                command=lambda id=juiz_id: self.confirmar_exclusao(id)
            ).grid(row=row, column=6, padx=5, pady=5)


    def confirmar_exclusao(self, juiz_id):
        chave_seguranca = "excluir/sim/registro/juiz" 

        dialog = customtkinter.CTkInputDialog(
            text=f"Tem certeza que deseja excluir o Juiz ID {juiz_id}?\nDigite a chave {chave_seguranca} para continuar:", 
            title="⚠️ Exclusão de Registros ⚠️"
        )
        
        input_text = dialog.get_input()

        if input_text == chave_seguranca:
            self.excluir_do_banco(juiz_id)
            
        elif input_text is not None:
            print("Chave de segurança incorreta. Exclusão cancelada.")


    def excluir_do_banco(self, juiz_id):
        banco_excel.excluir_juiz(juiz_id)
        print(f"Registro do Juiz ID {juiz_id} excluído com sucesso.")
        self.desenhar_tabela()
        self.atualizar_total_juiz()
        self.atualiza_metricas()
        
    def limpar_juiz(self):
        for nome_campo, campo in self.form_entries.items():
    
            if isinstance(campo, customtkinter.CTkEntry):
                campo.delete(0, 'end')

            elif isinstance(campo, customtkinter.CTkOptionMenu):
                if 'país' in nome_campo:
                    campo.set("Selecione o país")
                elif 'cargo' in nome_campo:
                    campo.set("Selecione o cargo")
                else:
                    campo.set(campo.cget("values")[0])
