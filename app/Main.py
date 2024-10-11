import tkinter as tk
from tkinter import font

from gui.main_window import MainWindow

def main():
    root = tk.Tk()
    #root.geometry("700x400")

    main = MainWindow(root)
    root.mainloop() # start the loop 
    


if __name__ == "__main__":
 main()