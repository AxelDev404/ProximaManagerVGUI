import tkinter as tk
from tkinter import font
import sys
import os
import sys
import os
from tkinter import Tk, Label, messagebox

sys.path.append(os.path.join(os.path.dirname(__file__), 'gui'))
from gui import MainWindow

def main():
    root = tk.Tk()
    
    main = MainWindow(root)
    root.mainloop() # start the loop 


if __name__ == "__main__":
    main()