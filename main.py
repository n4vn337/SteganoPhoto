from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root=Tk()
root.title('SteganoPhoto')
root.geometry('700x550+150+180')
root.resizable(False,False)
root.configure(bg="#2f4155")


#icon
image_icon=PhotoImage(file='secure.png')
root.iconphoto(False,image_icon)

#logo
logo_image = Image.open('secure.png')
logo_image = logo_image.resize((50, 50), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo_image)
Label(root,image=logo,bg='#2f4155').place(x=10,y=10)

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetypes=(('PNG file','*.png'),('JPG file','*.jpg'),('ALl file','*.txt')))

    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
def hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)

def show():
    clearMessage=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clearMessage)

def save():
    secret.save('hidden.png')


Label(root,text='SteganoPhoto',bg='#2d4155',fg='white',font='arial 25 bold').place(x=100,y=20)

#first frame
f=Frame(root,bd=3,bg='black',width=340,height=340,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg='black')
lbl.place(x=40,y=40)

#second frame
f2=Frame(root,bd=3,bg='white',width=340,height=340,relief=GROOVE)
f2.place(x=350,y=80)

text1=Text(f2,font='robote 20',bg='white',fg='black',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# third frame
f3=Frame(root,bd=3,bg='#2f4155',width=330,height=100,relief=GROOVE)
f3.place(x=10,y=430)

Button(f3,text='Open Image',width=10,height=2,font='arial 14 bold',command=showimage).place(x=20,y=30)
Button(f3,text='Save Image',width=10,height=2,font='arial 14 bold',command=save).place(x=180,y=30)
Label(f3,text='Picture, Image, Photo File',bg='#2f4155',fg='yellow').place(x=20,y=5)

# fourth frame
f4=Frame(root,bd=3,bg='#2f4155',width=330,height=100,relief=GROOVE)
f4.place(x=360,y=430)

Button(f4,text='Encode',width=10,height=2,font='arial 14 bold',command=hide).place(x=20,y=30)
Button(f4,text='Decode',width=10,height=2,font='arial 14 bold',command=show).place(x=180,y=30)

root.mainloop()
