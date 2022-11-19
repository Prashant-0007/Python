#from tkinter import *
import tkinter

def main():
    root_window = tkinter.Tk() 
    root_window.title("Hello GUI expanded version")

    label_widget = tkinter.Label(root_window) 
    label_widget.configure(text = "Welcome to batch 45 of CoreCode Programming Academy")
    label_widget.pack(side = tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
    
    root_window.mainloop()
if __name__ == "__main__":
    main() 
