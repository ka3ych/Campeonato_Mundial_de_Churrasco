from PIL import Image, ImageTk
import customtkinter

def load_icons():
    return {

        "home_icon": customtkinter.CTkImage(light_image=Image.open("./img/icons/home_dark.png"),
                                            dark_image=Image.open("./img/icons/home_light.png"),
                                            size=(20, 20)),

        "group_users_icon": customtkinter.CTkImage(light_image=Image.open("./img/icons/users_dark.png"),
                                                    dark_image=Image.open("./img/icons/users_light.png"),
                                                    size=(20, 18)),

        "juizes_icon": customtkinter.CTkImage(light_image=Image.open("./img/icons/juiz_dark.png"),
                                                dark_image=Image.open("./img/icons/juiz_light.png"),
                                                size=(20, 20))
    }