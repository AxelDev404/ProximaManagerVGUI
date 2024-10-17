import tkinter as tk
from tkinter import font

from gui.main_window import MainWindow
from gui.dashboard import DashBoard

def main():
    root = tk.Tk()
    
    main = MainWindow(root)
    root.mainloop() # start the loop 
    


if __name__ == "__main__":
 main()