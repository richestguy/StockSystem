from tkinter import *
from tkinter import ttk
import check_login
class LoginGUI:
    """
    Classe que representa a interface gráfica de um formulário de login.
    """

    def __init__(self):
        """
        Inicializa a janela principal e configura os estilos e widgets.
        """
        self.root = Tk()
        self.root.geometry("301x145")
        self.root.resizable(False, False)
        self.root.configure(background="white")
        self.root.title("Login Form")
        self.configure_styles()
        self.create_widgets()
        self.status = None
    def configure_styles(self):
        """
        Configura os estilos dos widgets utilizando o ttk.Style.
        """
        self.root.iconphoto(False, PhotoImage(file="./image.png"))
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("TButton", padding=6, relief="flat", background="#ccc")
        self.style.map("TButton", background=[("active", "lightblue"), ("pressed", "red")])
        self.style.configure("Label", background="white", foreground="black", font=("Arial", 12))
        self.root.configure(background="white")

    def create_widgets(self):
        """
        Cria e posiciona os widgets na janela principal.
        """
        

        self.login_label = ttk.Label(self.root, text="Username:", style="Label")
        self.login_label.grid(row=0, column=0, padx=10)
        self.login_entry = ttk.Entry(self.root, width=30)
        self.login_entry.grid(row=0, column=1, padx=10)

        self.passwd_label = ttk.Label(self.root, text="Password:", style="Label")
        self.passwd_label.grid(row=1, column=0, padx=10, pady=10)
        self.passwd_entry = ttk.Entry(self.root, width=30, show="x")
        self.passwd_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = ttk.Button(self.root, text="Login", command=lambda: self.check_login(), style="TButton")
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def check_login(self):
        """
        Verifica as credenciais inseridas e define o status de login.
        """
        
        username = self.login_entry.get().strip()
        password = self.passwd_entry.get().strip()
        if username and password:
            self.status = check_login.check_login(username, password)
            if self.status == 200:
                self.root.destroy()
            elif self.status == 401:
                if hasattr(self, 'info_label'):
                    self.info_label.destroy()
                self.info_label = ttk.Label(self.root, text="Invalid credentials. Please try again.", foreground="red", background="white")
                self.info_label.grid(row=3, column=0, columnspan=2)
            else:
                if hasattr(self, 'info_label'):
                    self.info_label.destroy()
                self.info_label = ttk.Label(self.root, text="An error occurred. Please try again later.", foreground="red", background="white")
                self.info_label.grid(row=3, column=0, columnspan=2)
        else:
            self.status = 400
            self.root.destroy()
    def run(self):
        """
        Inicia o loop principal da interface gráfica.
        """
        self.root.mainloop()
if __name__ == "__main__":
    app = LoginGUI()
    app.run()
    status = app.status
    