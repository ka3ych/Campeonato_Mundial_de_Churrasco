import customtkinter

class InitialFrame(customtkinter.CTkFrame):
    def __init__(self, parent, show_main_app, images):
        super().__init__(parent, corner_radius=0)
        self.grid_rowconfigure(0, weight=1) 
        self.grid_rowconfigure(5, weight=1) 
        self.grid_columnconfigure(0, weight=1)

        self.image_label = customtkinter.CTkLabel(
            self, 
            text="", 
            image=images["meme"])
        self.image_label.grid(row=1, column=0, padx=10, pady=20)

        self.title_label = customtkinter.CTkLabel(
            self,
            text="Campeonato Mundial\nDe Churrasco",
            font=customtkinter.CTkFont(size=40, weight="bold")
        )
        self.title_label.grid(row=2, column=0, padx=20, pady=20)

        self.title_label = customtkinter.CTkLabel(
            self,
            text="Seja bem-vindo ao sistema oficial do Churras dot com!\n Prepare-se para controlar tudo com facilidade: \ncadastro de participantes, juízes e resultados.",
            font=customtkinter.CTkFont(size=16, weight="bold")
        )
        self.title_label.grid(row=3, column=0, padx=20, pady=20)

        self.start_button = customtkinter.CTkButton(
            self,
            text="Iniciar Gerenciamento",
            width=300,
            height=50,
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=show_main_app
        )
        self.start_button.grid(row=4, column=0, padx=20, pady=20)