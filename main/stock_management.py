from tkinter import *
from tkinter import ttk 
import sys
sys.path.append("./db")
import removedb, nomedb, insertdb

def add_item(app):
        if hasattr(app, 'info_label'):
            app.info_label.destroy()

        app.status = insertdb.add_item(app.add_entry.get())   
        if app.status == 200:
             app.info_label = ttk.Label(app.add_root, text="Item adcionado com sucesso")
             for i in range(2):
                 app.stock_management()
        elif app.status == 409:
            app.info_label = ttk.Label(app.add_root, text="Item ja existe no banco de dados.")
        else:
            app.info_label = ttk.Label(app.add_root, text="Erro ao adcionar item.")
        app.info_label.pack()
def add_frame(app):
        app.add_root = Toplevel(app.root)
        app.add_root.title("Adcionar item")
        app.add_root.geometry("300x300")
        app.add_root.resizable(False,False)
        

        app.add_label = ttk.Label(app.add_root, text="Nome do item", font=("Arial", 12))
        app.add_entry = ttk.Entry(app.add_root)
       
        app.add_button = ttk.Button(app.add_root, text="Adcionar Item", command=lambda: add_item(app))
       
        app.add_label.pack( expand=True)
        app.add_entry.pack(expand=True)
        app.add_button.pack( expand=True)
def remove_item(app):
        if hasattr(app, 'info_label'):
            app.info_label.destroy()

        app.status = removedb.remove_item(app.remove_entry.get())
        if app.status == 200:
            app.info_label = ttk.Label(app.remove_root, text="Item removido com sucesso")
            for i in range(2):
                app.stock_management()
        elif app.status == 404:
            app.info_label = ttk.Label(app.remove_root, text="Item não encontrado.")
        else:
            app.info_label = ttk.Label(app.remove_root, text="Erro ao remover item.")
        app.info_label.pack()
def remove_frame(app):
        app.remove_root = Toplevel(app.root)
        app.remove_root.title("Remover Item")
        app.remove_root.geometry("300x300")
        app.remove_root.resizable(False,False)

        app.remove_label = ttk.Label(app.remove_root, text="Nome do item", font=("Arial", 12))
        app.remove_entry = ttk.Entry(app.remove_root)
        app.remove_button = ttk.Button(app.remove_root, text="Remover Item", command=lambda: remove_item(app))

        app.remove_label.pack(expand=True)
        app.remove_entry.pack(expand=True)
        app.remove_button.pack(expand=True)