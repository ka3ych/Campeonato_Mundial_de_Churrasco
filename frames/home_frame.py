import customtkinter

class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, parent, images):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        
        # frame da home - Visão Geral do Campeonato
        self.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(
            self,
            text="Visão Geral do Campeonato",
            font=customtkinter.CTkFont(size=40, weight="bold")
        )

        self.title.grid(row=0, column=0, padx=20, pady=10)

        self.image_label = customtkinter.CTkLabel(
            self, 
            text="", 
            image=images["churrasco"])
        self.image_label.grid(row=0, column=1, padx=(10, 200), pady=10)

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
        self.text = customtkinter.CTkLabel(
            self,
            text="⚠️ ⚠️ Página em desenvolvimento ⚠️ ⚠️",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            text_color="#E30000"
        )
        self.text.grid(row=1, column=0, padx=100, pady=100)