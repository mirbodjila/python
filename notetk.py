from tkinter import *
from tkinter import filedialog


window=Tk()
window.title("Notepad")
window.geometry("600x600")
window.resizable(False,False)
#function
def new_file():
    text_box.delete(1.0,END)

def open_file():
    file=filedialog.askopenfile(mode="r",filetypes=[('text file','*.text')])
    if file is not None:
        content=file.read()
    text_box.insert(INSERT,content)    


def save_file():
    open_file=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    txt=str(text_box.get(1.0,END))
    open_file.write(txt)
    open_file.close()
       
def copy():
       text_box
    


def cut():
    pass


def paste():
    pass



menubar = Menu(window)
window.config(menu=menubar,bg="lightblue")
file_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=window.destroy)
edit_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Copy",command=lambda:window.focus_get().event_generate('<<Copy>>'))
edit_menu.add_command(label="Cut",command=lambda:window.focus_get().event_generate('<<Cut>>'))

edit_menu.add_command(label="Paste",command=lambda:window.focus_get().event_generate('<<Paste>>'))
help_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About")
#textbox
text_box = Text(window,height="38",width="75",wrap=WORD)
text_box.place(x=0,y=0)


window.mainloop()