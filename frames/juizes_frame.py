import customtkinter

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
    
        
        self.filtro_pais = customtkinter.CTkOptionMenu(
            self.frame_filtros,
            dynamic_resizing=True,
            height=40,
            values=["Todos", "Brasil", "Espanha", "Estados Unidos"] #aqui será de acordo com os países que serão colocados na tabela -> modificar depois
        )
        self.filtro_pais.set("Filtrar por país")
        self.filtro_pais.grid(row=0, column=0, padx=(0, 5), pady=(10,10), sticky="w")

        self.filtro_cargo = customtkinter.CTkOptionMenu(
            self.frame_filtros,
            dynamic_resizing=True,
            height=40,
            values=["Todos", "Chef Executivo", "Mestre Churrasqueiro", "Crítica Gatronômica"] #aqui será de acordo com os países que serão colocados na tabela -> modificar depois
        )
        self.filtro_cargo.set("Filtrar por cargo")
        self.filtro_cargo.grid(row=0, column=1, padx=(0,5), pady=(10,10), sticky="w")

        self.entry = customtkinter.CTkEntry(
            self.frame_filtros, 
            placeholder_text="Pesquisar por nome...", 
            height=40,
            fg_color = "transparent"
        )
        self.entry.grid(row=0, column=2, padx=(0,5), columnspan=3, pady=(10, 10), sticky="ew")

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
        customtkinter.CTkLabel(self.total_card, text="Total de Juízes", font=customtkinter.CTkFont(size=14)).pack(padx=10, pady=5)
        customtkinter.CTkLabel(self.total_card, text="9", font=customtkinter.CTkFont(size=36, weight="bold")).pack(padx=10, pady=10) # ALTERAR DEPOIS PARA DEIXAR DINÂMICO

        # Placeholder para Gráfico 1 (Juízes por País) -> ARRUMAR
        self.chart1_card = customtkinter.CTkFrame(self.frame_analitico, fg_color="#AB00D1")
        self.chart1_card.grid(row=0, column=1, padx=(0, 20), sticky="nsew")
        customtkinter.CTkLabel(self.chart1_card, text="[ Gráfico: Juízes por País ]").pack(padx=10, pady=20)
        
        # Placeholder para Gráfico 2 (Juízes por Cargo) -> ARRUMAR
        self.chart2_card = customtkinter.CTkFrame(self.frame_analitico, fg_color="#00B9D1")
        self.chart2_card.grid(row=0, column=2, sticky="nsew")
        customtkinter.CTkLabel(self.chart2_card, text="[ Gráfico: Juízes por Cargo ]").pack(padx=10, pady=20)


        # FRAME PARA A TABELA
        self.table_frame = customtkinter.CTkScrollableFrame(
            self.div_principal, 
            corner_radius=0,
            height=250
        )
        
        self.table_frame.grid(row=3, column=0, columnspan=12, padx=20, pady=(10, 20), sticky="nsew")

        # Crie os cabeçalhos da tabela
        headers = ["ID_Juiz", "Nome", "País", "Cargo", "Data de Admissão"]
        for col, header in enumerate(headers):
            header_label = customtkinter.CTkLabel(
                self.table_frame, 
                text=header, 
                font=customtkinter.CTkFont(weight="bold")
            )
            header_label.grid(row=0, column=col, padx=10, pady=5, sticky="w")
            self.table_frame.grid_columnconfigure(col, weight=1)

        # Dados de exemplo para a tabela
        juizes_data = [
            {"id": 1, "nome": "João Silva", "pais": "Brasil", "cargo": "Chef Executivo", "data": "12/09/2020"},
            {"id": 2, "nome": "Maria Garcia", "pais": "Espanha", "cargo": "Crítica Gastronômica", "data": "15/03/2010"},
            {"id": 3, "nome": "Peter Jones", "pais": "Estados Unidos", "cargo": "Mestre Churrasqueiro", "data": "30/11/2019"},
            {"id": 4, "nome": "João Silva", "pais": "Brasil", "cargo": "Chef Executivo", "data": "12/09/2020"}
        ]

        # Adicione os juízes à tabela
        for i, juiz in enumerate(juizes_data):
            row = i + 1

            customtkinter.CTkLabel(self.table_frame, text=juiz["id"]).grid(row=row, column=0, padx=10, pady=5)
            customtkinter.CTkLabel(self.table_frame, text=juiz["nome"]).grid(row=row, column=1, padx=10, pady=5)
            customtkinter.CTkLabel(self.table_frame, text=juiz["pais"]).grid(row=row, column=2, padx=10, pady=5)
            customtkinter.CTkLabel(self.table_frame, text=juiz["cargo"]).grid(row=row, column=3, padx=10, pady=5)
            customtkinter.CTkLabel(self.table_frame, text=juiz["data"]).grid(row=row, column=4, padx=10, pady=5)

            # Botões de Ação
            customtkinter.CTkButton(self.table_frame, text="Editar", width=60, fg_color="#00BF6E").grid(row=row, column=5, padx=5, pady=5)
            customtkinter.CTkButton(self.table_frame, text="Excluir", width=60, fg_color="#E30000", command=self.open_dialog_event).grid(row=row, column=6, padx=5, pady=5)
        
        # ELEMENTOS DO PAINEL LATERAL PARA CADASTRO DE UM NOVO JUIZ
        form_title = customtkinter.CTkLabel(
            self.painel_lateral,
            text="Adicionar Novo Juiz",
            font=customtkinter.CTkFont(size=25, weight="bold")
        )
        form_title.grid(row=1, column=0, padx=20, pady=(5, 10), sticky="ew")

        campos = [
            ("Nome", "Digite o nome completo", "entry"),
            ("País", "Selecione o país", "dropdown", ["Brasil", "Espanha", "Estados Unidos"]),
            ("Cargo", "Selecione o cargo", "dropdown", ["Che Executivo", "Mestre Churrasqueiro", "Crítica Gastronômica"]),
            ("Telefone", "(00) 00000-0000", "entry"),
            ("Data de Nascimento", "dd/mm/aaaa", "entry")
        ]

        self.image_label = customtkinter.CTkLabel(
            self.painel_lateral, 
            text="", 
            image=images["jurado"])
        self.image_label.grid(row=0, column=0, padx=10, pady=(0,5))

        self.form_entries = {}

        for i, (label_text, placeholder, tipo, *opcoes) in enumerate(campos):
            label = customtkinter.CTkLabel(
                self.painel_lateral, 
                text=label_text
            )
            label.grid(row=2*i + 2, column=0, padx=20, pady=(10,0), sticky="w")

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
            entrada.grid(row=2*i + 3, column=0, padx=20, pady=(5, 10), sticky="ew")
            self.form_entries[label_text.lower().replace(" ", "_")] = entrada

            # Botão de Adicionar
            self.salvar_button = customtkinter.CTkButton(
                self.painel_lateral, 
                text="Salvar Juiz", 
                fg_color="#00BF6E", 
                height=40,
                # command=self.salvar_juiz # Conectar depois à sua função de salvar no banco de dados
            )
            self.salvar_button.grid(row=len(campos)*2 + 4, column=0, padx=20, pady=(30, 10), sticky="ew")

            # Botão de Limpar/Cancelar
            self.limpar_button = customtkinter.CTkButton(
                self.painel_lateral, 
                text="Limpar Campos", 
                fg_color="#3EB599",
                height=40,
                command=self.limpar_juiz
            )
            self.limpar_button.grid(row=len(campos)*2 + 5, column=0, padx=20, pady=(0, 20), sticky="ew")





    def open_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Tem certeza que deseja excluir esse registro?\nDigite fwifljljeopwr pra continuar", 
            title="⚠️ Exclusão de Registros ⚠️")
        print("CTkInputDialog:", dialog.get_input()
    )
        
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
    