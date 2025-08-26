from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from nomedb import get_produtos
import insertdb

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tempero Rios Stock Management System")
        self.configure_styles()
        self.nav_bar()
        
    def configure_styles(self):

        self.root.iconphoto(False, PhotoImage(file="./image.png"))
        self.root.geometry("800x600")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.root.resizable(False, False)
        self.root.configure(background="black")
        
    def nav_bar(self):
        self.nav = Frame(self.root, bg="blue", borderwidth=2, relief="solid")
        self.img = Image.open("./image.png")
        self.img = self.img.resize((50, 50))
        self.imagem = ImageTk.PhotoImage(self.img)
        

        
        self.logo_label = ttk.Label(self.nav, image=self.imagem, background="white",  )
        self.nav_label = ttk.Label(self.nav, text="Navigation")
        self.button1 = ttk.Button(self.nav, text="Stock Management", command=lambda: self.stock_management())

       
        self.logo_label.pack(side=TOP, padx=5, pady=5)
        self.nav_label.pack(side=TOP, padx=5, pady=5)
        self.button1.pack(side=TOP, padx=5, pady=5)
        self.nav.pack(side=LEFT, fill=Y)
    
    def on_search(self):
        self.searchstr = self.filter_bar_entry.get()
        
        if self.searchstr in self.produtos:
            self.stock_label.destroy()
            self.stock_label = ttk.Label(self.stock_frame_bottom, text=self.searchstr, background="white", font=("Arial", 12))
            self.stock_label.pack(anchor="w",  padx=5, pady=5)
        elif not self.searchstr:
            self.stock_label.destroy()
            self.stock_label = ttk.Label(self.stock_frame_bottom, text="\n".join(self.produtos), background="white", font=("Arial", 12))
            self.stock_label.pack(anchor="w", padx=10, pady=10)
        else:
            self.stock_label.destroy()
            self.stock_label = ttk.Label(self.stock_frame_bottom, text="Item nao encontrado.", background="white", font=("Arial", 12))
            self.stock_label.pack(side=TOP)
    
    
    def add_item(self):
        if hasattr(self, 'info_label'):
            self.info_label.destroy()

        self.status = insertdb.add_item(self.add_entry.get())   
        if self.status == 200:
             self.info_label = ttk.Label(self.add_root, text="Item adcionado com sucesso")
             for i in range(2):
                 self.stock_management()
        elif self.status == 409:
            self.info_label = ttk.Label(self.add_root, text="Item ja existe no banco de dados.")
        else:
            self.info_label = ttk.Label(self.add_root, text="Erro ao adcionar item.")
        self.info_label.pack()
    def add_frame(self):
        self.add_root = Toplevel(self.root)
        self.add_root.title("Adcionar item")
        self.add_root.geometry("300x300")
        self.add_root.resizable(False,False)
        

        self.add_label = ttk.Label(self.add_root, text="Nome do item", font=("Arial", 12))
        self.add_entry = ttk.Entry(self.add_root)
       
        self.add_button = ttk.Button(self.add_root, text="Adcionar Item", command=lambda: self.add_item())
       
        self.add_label.pack( expand=True)
        self.add_entry.pack(expand=True)
        self.add_button.pack( expand=True)
    
   
    
    def remove_frame(self):
        self.remove_root = Toplevel(self.root)
        self.remove_root.title("Remover Item")
        self.remove_root.geometry("300x300")
        self.remove_root.resizable(False,False)

        self.remove_label = ttk.Label(self.remove_root, text="Nome do item", font=("Arial", 12))
        self.remove_entry = ttk.Entry(self.remove_root)
        self.remove_button = ttk.Button(self.remove_root, text="Remover Item", command=self.remove_item)

        self.remove_label.pack(expand=True)
        self.remove_entry.pack(expand=True)
        self.remove_button.pack(expand=True)

    def stock_management(self):
        

        
        if hasattr(self, 'stock_frame_bottom') and self.stock_frame_bottom.winfo_exists():
            self.stock_frame_bottom.destroy()
            self.stock_frame.destroy()
            return
        
        self.produtos = [item[0] for item in get_produtos()]
        self.stock_frame = Frame(self.root, bg="black")
        self.stock_frame_bottom = Frame(self.root,bg="white")

        self.filter_bar_entry = ttk.Entry(self.stock_frame, background="black")
        
        self.filter_bar_button  = ttk.Button(self.stock_frame, text="Search", command=lambda: self.on_search())
        self.removeitem = ttk.Button(self.stock_frame, text="Remover", command=lambda: self.remove_frame())
        self.additem = ttk.Button(self.stock_frame, text="Adcionar", command=lambda: self.add_frame())
        
        
       

        

            
        self.stock_label = ttk.Label(self.stock_frame_bottom, text="\n".join(self.produtos), font=('Arial', 12), background="white")
        
        self.additem.pack(side=RIGHT, padx=10, pady=10)
        self.removeitem.pack(side=RIGHT, padx=10, pady=10)
        self.filter_bar_button.pack(side=RIGHT)
        self.filter_bar_entry.pack(side=RIGHT)
        self.stock_label.pack(anchor="w", padx=5, pady=5, )
        self.stock_frame.pack(side=TOP, fill=X, padx=10, pady=10)
        self.stock_frame_bottom.pack(side=TOP, fill=BOTH, expand=True)

    def run(self):
        """
        Inicia o loop principal da interface gráfica.
        """
        self.root.mainloop()
if __name__ == "__main__":
    app = Gui()
    app.run()
        