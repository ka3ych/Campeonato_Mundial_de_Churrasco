import customtkinter

class TeamFrame(customtkinter.CTkFrame):
    def __init__(self, parent, images):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(
            self, 
            text="Gerenciamento de Equipes",
            font=customtkinter.CTkFont(size=40, weight="bold"))
    
        self.title.grid(row=0, column=0, padx=20, pady=10)

        self.image_label = customtkinter.CTkLabel(
            self, 
            text="", 
            image=images["team"])
        
        self.image_label.grid(row=0, column=1, padx=(10, 200), pady=10)