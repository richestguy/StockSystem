from logingui import LoginGUI
import sys
sys.path.append("./main")
from gui import Gui #type: ignore



login = LoginGUI()
login.run()
status = login.status
if status == 200:
    gui= Gui()
    print("Login successful!")
    gui.run()
else:
    print("Login failed!")
    
