import customtkinter as ctk

from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("Pass Gen")
        self.resizable(False, False)

        self.logo = ctk.CTkImage(dark_image=Image.open("static/img/logo.png"), size=(460, 150))


if __name__ == "__main__":
    app = App()
    app.mainloop()
