from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as font
import backend
from datetime import datetime as dt
window=Tk()
window.geometry("465x325")
window.iconbitmap("book.ico")
C=Canvas(window, bg='blue', height=250, width=465)
filename=PhotoImage(file='1562322358669.png')
bg_l=Label(window, image=filename)
bg_l.place(x=0, y=0, relwidth=1, relheight=1)
C.grid(row=0,column=0,rowspan=11,columnspan=10)
window.wm_title("Mom Note")

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    #Drop.delete(0,END)
    #Drop.insert(END,selected_tuple[5])


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(dt_text.get(),name_text.get(),colour_text.get(),count_text.get(),var.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(dt.now(),name_text.get(),colour_text.get(),count_text.get(),var.get())
    list1.delete(0,END)
    list1.insert(END,(dt.now(),name_text.get(),colour_text.get(),count_text.get(),var.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],dt.now(),name_text.get(),colour_text.get(),count_text.get(),var.get())


#Labels
labFont=font.Font(family='Courier New Greek',size=8,weight='bold')
l1=Label(window,text='DateTime',bg='light green',bd=3,relief='ridge')
l1['font']=labFont
l1.grid(row=0,column=2)

l2=Label(window,text='Name',bg='light green',bd=3,relief='ridge')
l2['font']=labFont
l2.grid(row=2,column=0)

l3=Label(window,text='Colour',bg='light green',bd=3,relief='ridge')
l3['font']=labFont
l3.grid(row=2,column=3)

l4=Label(window,text='Count',bg='light green',bd=3,relief='ridge')
l4['font']=labFont
l4.grid(row=3,column=0)

l5=Label(window,text='Status',bg='light green',bd=3,relief='ridge')
l5['font']=labFont
l5.grid(row=3,column=3)


#Entry's
e1=Entry(window,bd=1,relief='solid',textvariable=dt.now())
e1.grid(row=1,column=2)

name_text=StringVar()
e2=Entry(window,bd=1,relief='solid',textvariable=name_text)
e2.grid(row=2,column=1)

colour_text=StringVar()
e3=Entry(window,bd=1,relief='solid',textvariable=colour_text)
e3.grid(row=2,column=4)

count_text=StringVar()
e4=Entry(window,bd=1,relief='solid',textvariable=count_text)
e4.grid(row=3,column=1)
#status_text=StringVar()
#e5=Entry(window,textvariable=status_text)
#e5.grid(row=3,column=4)

#ListBox
list1=Listbox(window,height=10,width=50,bd=5,relief='raised',bg='wheat1')
list1.grid(row=4,column=0,rowspan=8,columnspan=3)

#ScrollBar
sb1=Scrollbar(window)
sb1.grid(row=5,column=3,rowspan=8)

#Configure
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#BIND
list1.bind("<<ListboxSelect>>",get_selected_row)

#Buttons
ButtFont=font.Font(family='Segoe Print',size=8,weight='bold')

b1=Button(window,text="View All",width=12,command=view_command,height=1,bg='sky blue')
b1['font']=ButtFont
b1.grid(row=7,column=4)

b2=Button(window,text="Add Entry",width=12,command=add_command,height=1,bg='sky blue')
b2['font']=ButtFont
b2.grid(row=8,column=4)

b3=Button(window,text="Search Entry",width=12,command=search_command,height=1,bg='sky blue')
b3['font']=ButtFont
b3.grid(row=9,column=4)

b4=Button(window,text="Update",width=12,command=update_command,height=1,bg='sky blue')
b4['font']=ButtFont
b4.grid(row=10,column=4)

b5=Button(window,text="Delete",width=12,command=delete_command,height=1,bg='sky blue')
b5['font']=ButtFont
b5.grid(row=11,column=4)

b6=Button(window,text="Close",width=12,command=window.destroy,height=1,bg='sky blue')
b6['font']=ButtFont
b6.grid(row=12,column=4)

#Dropdown Menu
Options=["Hemming" , "Folding" , "Tying" , "Other"]
var=StringVar(window)
var.set(Options[0])
Drop=OptionMenu(window,var,*Options)
Drop.grid(row=3,column=4)
"""
C=Canvas(window, bg='blue', height=800, width=500)
filename=PhotoImage(file='1562306781504.png')
bg_l=Label(window, image=filename)
bg_l.place(x=0, y=0, relwidth=1, relheight=1)
C.grid(row=0,column=0,rowspan=11,columnspan=10)
"""
"""
mi = ImageTk.PhotoImage(Image.open("1562306781504.png"))
mi_l = Label(image=mi)
mi_l.grid(row=0,column=0)
"""
"""
photo=PhotoImage(file='1562306781504.png')
w=Label(window,image=photo)
ent=Entry(window)
w.grid(row=0,column=0,rowspan=11,columnspan=10)
ent=Entry(window)
ent.grid(row=0,column=0,rowspan=11,columnspan=10)
ent.focus_set()
"""
window.mainloop()
