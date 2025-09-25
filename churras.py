import customtkinter
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Campeonato Mundial de Churrasco")
        
	# --- Obtendo a resolução da tela ---
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        
        # Define o tamanho inicial da janela como o tamanho da tela
        self.geometry(f"{largura_tela}x{altura_tela}")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        self.logo_image = customtkinter.CTkImage(Image.open("img/carne-logo.png"), size=(60, 60))

        self.churrasco_img = customtkinter.CTkImage(Image.open("img/churra.png"), size=(180, 180))
        self.team_anima = customtkinter.CTkImage(Image.open("img/equipe_anima.gif"), size=(210, 180))

        self.image_icon_image = customtkinter.CTkImage(Image.open("img/carne-logo.png"), size=(20, 20))

        self.home_image = customtkinter.CTkImage(light_image=Image.open("img/icons/home_dark.png"),
                                                 dark_image=Image.open("img/icons/home_light.png"), size=(20, 20))

        self.group_of_users_image = customtkinter.CTkImage(light_image=Image.open("img/icons/users_dark.png"),
                                                 dark_image=Image.open("img/icons/users_light.png"), size=(20, 18))

        self.juizes_image = customtkinter.CTkImage(light_image=Image.open("img/icons/juiz_dark.png"),
                                                     dark_image=Image.open("img/icons/juiz_light.png"), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Campeonato Mundial\nDe Churrasco", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Equipes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.group_of_users_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Juízes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.juizes_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # frame da home - Visão Geral do Campeonato
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_title = customtkinter.CTkLabel(self.home_frame, text="Visão Geral do Campeonato",
                                                  font=customtkinter.CTkFont(size=40, weight="bold"))
        self.home_frame_title.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.churrasco_img)
        self.home_frame_large_image_label.grid(row=0, column=1, padx=(10, 200), pady=10)

        """
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)
        """

        # frame para equipes e competidores
        self.team_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.team_frame.grid_columnconfigure(0, weight=1)

        self.team_frame_title = customtkinter.CTkLabel(self.team_frame, text="Gerenciamento de Equipes",
                                                  font=customtkinter.CTkFont(size=40, weight="bold"))
    
        self.team_frame_title.grid(row=0, column=0, padx=20, pady=10)

        self.team_frame_large_image_label = customtkinter.CTkLabel(self.team_frame, text="", image=self.team_anima)
        self.team_frame_large_image_label.grid(row=0, column=1, padx=(10, 200), pady=10)
        
        # frame para listagem dos juízes
        self.juiz_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.juiz_frame.grid_columnconfigure(0, weight=1)

        self.juiz_frame_title = customtkinter.CTkLabel(self.juiz_frame, text="Gerenciamento de Juízes",
                                                  font=customtkinter.CTkFont(size=40, weight="bold"))
    
        self.juiz_frame_title.grid(row=0, column=0, padx=20, pady=10)
        

        self.juiz_entry = customtkinter.CTkEntry(self.juiz_frame, placeholder_text="Digite sua pesquisa", width=300)
        self.juiz_entry.grid(row=1, column=0, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.juiz_optionmenu = customtkinter.CTkOptionMenu(self.juiz_frame, dynamic_resizing=False, values=["Nome", "País", "Cargo"])
        self.juiz_optionmenu.grid(row=1, column=1, padx=(20,0), pady=(20, 20))

        self.juiz_entry_button = customtkinter.CTkButton(master=self.juiz_frame, text="Search", fg_color="#0073BA", border_width=0)
        self.juiz_entry_button.grid(row=1, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.juiz_add_button = customtkinter.CTkButton(master=self.juiz_frame, text="Adicionar Novo Juiz", fg_color="#0073BA", border_width=0)
        self.juiz_add_button.grid(row=1, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Crie o frame de rolagem para a tabela
        self.juizes_table_frame = customtkinter.CTkScrollableFrame(self.juiz_frame, corner_radius=0)
        self.juizes_table_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Crie os cabeçalhos da tabela
        headers = ["ID_Juiz", "Nome", "País", "Cargo", "Data de Admissão"]
        for col, header in enumerate(headers):
            header_label = customtkinter.CTkLabel(self.juizes_table_frame, text=header, font=customtkinter.CTkFont(weight="bold"))
            header_label.grid(row=0, column=col, padx=10, pady=5)
            self.juizes_table_frame.grid_columnconfigure(col, weight=1)

        # Dados de exemplo para a tabela
        juizes_data = [
            {"id": 1, "nome": "João Silva", "pais": "Brasil", "cargo": "Chef Executivo", "data": "12/09/2020"},
            {"id": 2, "nome": "Maria Garcia", "pais": "Espanha", "cargo": "Crítica Gastronômica", "data": "15/03/2010"},
            {"id": 3, "nome": "Peter Jones", "pais": "Estados Unidos", "cargo": "Mestre Churrasqueiro", "data": "30/11/2019"}
        ]

        # Adicione os juízes à tabela
        for i, juiz in enumerate(juizes_data):
            row = i + 1

            id_label = customtkinter.CTkLabel(self.juizes_table_frame, text=juiz["id"])
            id_label.grid(row=row, column=0, padx=10, pady=5)

            nome_label = customtkinter.CTkLabel(self.juizes_table_frame, text=juiz["nome"])
            nome_label.grid(row=row, column=1, padx=10, pady=5)

            pais_label = customtkinter.CTkLabel(self.juizes_table_frame, text=juiz["pais"])
            pais_label.grid(row=row, column=2, padx=10, pady=5)

            cargo_label = customtkinter.CTkLabel(self.juizes_table_frame, text=juiz["cargo"])
            cargo_label.grid(row=row, column=3, padx=10, pady=5)

            data_label = customtkinter.CTkLabel(self.juizes_table_frame, text=juiz["data"])
            data_label.grid(row=row, column=4, padx=10, pady=5)

            # Botões de Ação
            edit_button = customtkinter.CTkButton(self.juizes_table_frame, text="Editar", width=60, fg_color="#00BF6E")
            edit_button.grid(row=row, column=5, padx=5, pady=5)

            delete_button = customtkinter.CTkButton(self.juizes_table_frame, text="Excluir", width=60, fg_color="#E30000", command=self.open_dialog_event)
            
            delete_button.grid(row=row, column=6, padx=5, pady=5)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.team_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.team_frame.grid_forget()
        if name == "frame_3":
            self.juiz_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.juiz_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def open_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Tem certeza que deseja excluir esse registro?\nDigite fwiflwfjskdvkljeopwr pra continuar", title="⚠️ Exclusão de Registros ⚠️")
        print("CTkInputDialog:", dialog.get_input())


if __name__ == "__main__":
    app = App()
    app.mainloop()

