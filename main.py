import customtkinter as ctk

from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("Passgen")
        self.resizable(False, False)

        self.logo = ctk.CTkImage(dark_image=Image.open("static/img/logo.png"), size=(460, 150))
        self.logo_label = ctk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20,20), sticky="new")

        self.entry_password = ctk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = ctk.CTkButton(master=self.password_frame, text="Generate",
                                          width=100, command=self.set_password)
        self.btn_generate.grid(row=0, column=1)

    def set_password(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
