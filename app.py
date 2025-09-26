import customtkinter

from frames.home_frame import HomeFrame
from frames.team_frame import TeamFrame
from frames.juizes_frame import JuizFrame
from frames.frame_inicial import InitialFrame
from utils.images import load_images
from utils.icons import load_icons

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Campeonato Mundial de Churrasco")

        # Obtendo a resoluç~çao da tela para que a janela ocupe a tela inteira ao carregar
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        self.geometry(f"{largura_tela}x{altura_tela}")

        # carregar imagens (função centralizada)
        self.images = load_images()
        self.icons = load_icons()

        # configurar grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # navigation frame
        self.create_navigation()

        # criar frames
        self.home_frame = HomeFrame(self, self.images)
        self.team_frame = TeamFrame(self, self.images)
        self.juiz_frame = JuizFrame(self, self.images)
        self.frame_inicial = InitialFrame(self, self.show_main_app, self.images)

        # frame inicial
        self.frame_inicial.grid(row=0, column=0, columnspan=2, sticky="nsew")

    def show_main_app(self):
        """Esconde a tela inicial e mostra a interface principal do app."""
        self.frame_inicial.grid_forget()

        # reconfigura o grid para a navegação
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.create_navigation()
        self.select_frame_by_name("home")

    def show_initial_frame(self):
        """Esconde o app e mostra a tela inicial."""
        self.navigation_frame.grid_forget()
        self.home_frame.grid_forget()
        self.team_frame.grid_forget()
        self.juiz_frame.grid_forget()

        # reconfigura o grid para ocupar a tela inteira com a tela inicial
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.frame_inicial.grid(row=0, column=0, columnspan=2, sticky="nsew")

    def create_navigation(self):
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.label = customtkinter.CTkLabel(
            self.navigation_frame, 
            text="Campeonato Mundial\nDe Churrasco",
            image=self.images["logo"],
            compound="top", 
            font=customtkinter.CTkFont(size=16, weight="bold"))
        
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.icons["home_icon"], anchor="w", 
            command=self.home_button_event
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.team_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Equipes",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.icons["group_users_icon"], anchor="w", 
            command=self.team_frame_event
        )
        
        self.team_button.grid(row=2, column=0, sticky="ew")

        self.juiz_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Juízes",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.icons["juizes_icon"], anchor="w", 
            command=self.juiz_frame_event
        )
        self.juiz_button.grid(row=3, column=0, sticky="ew")

        self.logout_btn = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=5, height=40, border_spacing=10, text="Logout",
            fg_color="#E33B14", hover_color="#B82100", anchor="w",
            command=self.show_initial_frame
        )
        self.logout_btn.grid(row=6, column=0, padx=10, pady=(0, 60), sticky="s")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame, 
            values=["Light", "Dark", "System"],
            height=40,
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_menu.grid(row=5, column=0, padx=10, pady=30, sticky="s")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.team_frame.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.juiz_frame.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

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

    def team_frame_event(self):
        self.select_frame_by_name("frame_2")

    def juiz_frame_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


    