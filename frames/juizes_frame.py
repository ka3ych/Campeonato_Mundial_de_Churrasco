import customtkinter

class JuizFrame(customtkinter.CTkFrame):
    def __init__(self, parent, images):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(
            self, 
            text="Gerenciamento de Juízes",
            font=customtkinter.CTkFont(size=40, weight="bold")
        )
    
        self.title.grid(row=0, column=0, padx=20, pady=10)
        

        self.entry = customtkinter.CTkEntry(
            self, 
            placeholder_text="Digite sua pesquisa", 
            width=300
        )
        
        self.entry.grid(row=1, column=0, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.optionmenu = customtkinter.CTkOptionMenu(
            self, 
            dynamic_resizing=False,
            values=["Nome", "País", "Cargo"]
        )
        
        self.optionmenu.grid(row=1, column=1, padx=(20,0), pady=(20, 20))

        self.search_button = customtkinter.CTkButton(
            self, 
            text="Search", 
            fg_color="#0073BA", 
            border_width=0
        )

        self.search_button.grid(row=1, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.add_button = customtkinter.CTkButton(
            self, 
            text="Adicionar Novo Juiz", 
            fg_color="#0073BA", 
            border_width=0
        )
        
        self.add_button.grid(row=1, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Crie o frame de rolagem para a tabela
        self.table = customtkinter.CTkScrollableFrame(
            self, 
            corner_radius=0
        )
        
        self.table.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Crie os cabeçalhos da tabela
        headers = ["ID_Juiz", "Nome", "País", "Cargo", "Data de Admissão"]
        for col, header in enumerate(headers):
            header_label = customtkinter.CTkLabel(self.table, text=header, font=customtkinter.CTkFont(weight="bold"))
            header_label.grid(row=0, column=col, padx=10, pady=5)
            self.table.grid_columnconfigure(col, weight=1)

        # Dados de exemplo para a tabela
        juizes_data = [
            {"id": 1, "nome": "João Silva", "pais": "Brasil", "cargo": "Chef Executivo", "data": "12/09/2020"},
            {"id": 2, "nome": "Maria Garcia", "pais": "Espanha", "cargo": "Crítica Gastronômica", "data": "15/03/2010"},
            {"id": 3, "nome": "Peter Jones", "pais": "Estados Unidos", "cargo": "Mestre Churrasqueiro", "data": "30/11/2019"},
            {"id": 4, "nome": "João Silva", "pais": "Brasil", "cargo": "Chef Executivo", "data": "12/09/2020"},
            {"id": 5, "nome": "Maria Garcia", "pais": "Espanha", "cargo": "Crítica Gastronômica", "data": "15/03/2010"},
            {"id": 6, "nome": "Peter Jones", "pais": "Estados Unidos", "cargo": "Mestre Churrasqueiro", "data": "30/11/2019"},
            {"id": 7, "nome": "João Silva", "pais": "Brasil", "cargo": "Chef Executivo", "data": "12/09/2020"},
            {"id": 8, "nome": "Maria Garcia", "pais": "Espanha", "cargo": "Crítica Gastronômica", "data": "15/03/2010"},
            {"id": 9, "nome": "Peter Jones", "pais": "Estados Unidos", "cargo": "Mestre Churrasqueiro", "data": "30/11/2019"}
        ]

        # Adicione os juízes à tabela
        for i, juiz in enumerate(juizes_data):
            row = i + 1

            customtkinter.CTkLabel(self.table, text=juiz["id"]).grid(row=row, column=0, padx=10, pady=5)
            customtkinter.CTkLabel(self.table, text=juiz["nome"]).grid(row=row, column=1, padx=10, pady=5)
            customtkinter.CTkLabel(self.table, text=juiz["pais"]).grid(row=row, column=2, padx=10, pady=5)
            customtkinter.CTkLabel(self.table, text=juiz["cargo"]).grid(row=row, column=3, padx=10, pady=5)
            customtkinter.CTkLabel(self.table, text=juiz["data"]).grid(row=row, column=4, padx=10, pady=5)

            # Botões de Ação
            customtkinter.CTkButton(self.table, text="Editar", width=60, fg_color="#00BF6E").grid(row=row, column=5, padx=5, pady=5)
            customtkinter.CTkButton(self.table, text="Excluir", width=60, fg_color="#E30000", command=self.open_dialog_event).grid(row=row, column=6, padx=5, pady=5)


    def open_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Tem certeza que deseja excluir esse registro?\nDigite fwifljljeopwr pra continuar", 
            title="⚠️ Exclusão de Registros ⚠️")
        print("CTkInputDialog:", dialog.get_input())