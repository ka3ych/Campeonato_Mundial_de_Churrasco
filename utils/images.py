from PIL import Image, ImageTk
import customtkinter

def load_images():
    return {
        "logo": customtkinter.CTkImage(Image.open("img/carne-logo.png"), size=(60, 60)),
        "churrasco": customtkinter.CTkImage(Image.open("img/churra.png"), size=(180, 180)),
        "team": customtkinter.CTkImage(Image.open("img/equipe_anima.gif"), size=(250, 180)),
        "meme": customtkinter.CTkImage(Image.open("img/meme.jpg"), size=(450, 270)),
        "jurado": customtkinter.CTkImage(Image.open("img/jurado.png"), size=(200, 200))
    }