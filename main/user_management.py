from tkinter import *
from tkinter import ttk
import sys
sys.path.append("./db")
import get_user, add_userdb, remove_userdb


def add_user(app):
    if hasattr(app, 'info_add_label'):
        app.info_add_label.destroy()
    app.username = app.add_user_entry.get()
    app.senha = app.add_password_entry.get()
    app.status = add_userdb.add_user(app.username, app.senha)
    if app.status == 200:
        app.info_add_label = ttk.Label(app.add_user_root, text="Usuario adcionado com sucesso")
        for i in range(2):
            app.user_management()
    elif app.status == 409:
        app.info_add_label = ttk.Label(app.add_user_root , text="Usuario ja existe no banco de dados.")
    else:
        app.info_add_label = ttk.Label(app.add_user_root , text="Erro ao adcionar usuario.")
    app.info_add_label.pack()
def add_user_frame(app):
    app.add_user_root = Toplevel(app.root)
    app.add_user_root.title("Add User")
    app.add_user_root.geometry("300x230")
    app.add_user_root.resizable(False,False)

    app.add_user_label = ttk.Label(app.add_user_root, text="Username", font=("Arial", 12))
    app.add_user_entry = ttk.Entry(app.add_user_root, font=("Arial", 12))
    app.add_password_label = ttk.Label(app.add_user_root, text="Password", font=("Arial", 12))
    app.add_password_entry = ttk.Entry(app.add_user_root, font=("Arial", 12), show="*")
    app.add_user_button = ttk.Button(app.add_user_root, text="Add User", command=lambda: add_user(app))

    app.add_user_label.pack(pady=10)
    app.add_user_entry.pack(pady=10)
    app.add_password_label.pack(pady=10)
    app.add_password_entry.pack(pady=10)
    app.add_user_button.pack(pady=10)

def remove_user(app):
        if hasattr(app, 'remove_info_label'):
            app.remove_info_label.destroy()
        app.usuario = app.remove_user_entry.get()
        app.status = remove_userdb.remove_user(app.usuario)
        if app.status == 200:
            app.remove_info_label = ttk.Label(app.remove_user_root, text="Usuario removido do sistema")
            for i in range(2):
                app.user_management()
        elif app.status == 409:
            app.remove_info_label = ttk.Label(app.remove_user_root, text="Usuario inexistente")
        else:
            app.remove_info_label = ttk.Label(app.remove_user_root, text="Erro desconhecido, tente novamente")
        app.remove_info_label.pack()
def remove_user_frame(app):
        app.remove_user_root = Toplevel(app.root)
        app.remove_user_root.title("Remove user")
        app.remove_user_root.geometry("300x220")
        app.remove_user_root.resizable(False,False)

        app.remove_user_label = ttk.Label(app.remove_user_root, text="Usuario:")
        app.remove_user_entry = ttk.Entry(app.remove_user_root)
        app.remove_user_button = ttk.Button(app.remove_user_root, text="Remover usuario", command=lambda: remove_user(app))

        app.remove_user_label.pack()
        app.remove_user_entry.pack()
        app.remove_user_button.pack()
    

