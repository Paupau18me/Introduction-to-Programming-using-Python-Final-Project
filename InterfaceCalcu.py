
import tkinter as tk

root = tk.Tk()
txt = tk.StringVar()
txt.set('')
num = tk.StringVar()
cnt = tk.IntVar()
para_div = tk.DoubleVar()
sw = tk.IntVar()
sw.set(0)
print(sw.get())
#1 -> suma
#2 -> resta
#3 -> prod
#4 -> div
def suma():
    cnt.set(0)
    cnt.set(int(txt.get()))
    txt.set('')
    sw.set(1)
def resta():
    cnt.set(0)
    cnt.set(int(txt.get()))
    txt.set('')
    sw.set(2)
def prod():
    cnt.set(1)
    cnt.set(int(txt.get()))
    txt.set('')
    sw.set(3)
def div():
    cnt.set(0)
    cnt.set(int(txt.get()))
    txt.set('')
    sw.set(4)
def resul():
    #con el if compara la ultima operacion
    if sw.get() == 1:
        cnt.set(cnt.get()+int(txt.get()))
        txt.set(str(cnt.get()))
    elif sw.get() == 2:
        cnt.set(cnt.get() - int(txt.get()))
        txt.set(str(cnt.get()))
    elif sw.get() == 3:
        cnt.set(cnt.get() * int(txt.get()))
        txt.set(str(cnt.get()))
    else:
        cnt.set(cnt.get() / int(txt.get()))#Esto lo dejo porque si lo quitaba ya no funcionaba :C Lo revisare despues
        para_div.set(cnt.get() / int(txt.get()))
        txt.set(str(para_div.get()))
def seteo(x):
    num.set(x)
    txt.set(txt.get() + num.get())
def one():
    seteo('1')
def two():
    seteo('2')
def three():
    seteo('3')
def four():
    seteo('4')
def five():
    seteo('5')
def six():
    seteo('6')
def seven():
    seteo('7')
def eight():
    seteo('8')
def nine():
    seteo('9')
def zero():
    seteo('0')
def eli():
    x = txt.get()[0:len(txt.get())-1]
    txt.set(x)

root.geometry('426x340')
root.title('Calculadora Feliz :D')

root.configure(bg="#28B463")

#Pantalla
tk.Label(root, textvariable=txt,bg='#ABEBC6', width= 20,fg='black',font=('',24)).place(x=62,y=50)

#1er ROW
tk.Button(root, text='7',bd=0,width=4,fg='#28B463',font=('',24),command=seven).place(x=62,y=100)
tk.Button(root, text='8',width=4,fg='#28B463',font=('',24),command=eight).place(x=142,y=100)
tk.Button(root, text='9',width=4,fg='#28B463',font=('',24),command=nine).place(x=222,y=100)
tk.Button(root, text='<',width=4,fg='#28B463',font=('',24),command=eli).place(x=302,y=100)

#2do ROW
tk.Button(root, text='4',bd=0,width=4,fg='#28B463',font=('',24),command=four).place(x=62,y=150)
tk.Button(root, text='5',width=4,fg='#28B463',font=('',24),command=five).place(x=142,y=150)
tk.Button(root, text='6',width=4,fg='#28B463',font=('',24),command=six).place(x=222,y=150)
tk.Button(root, text='÷',width=4,fg='#28B463',font=('',24),command=div).place(x=302,y=150)

#3er ROW
tk.Button(root, text='1',bd=0,width=4,fg='#28B463',font=('',24),command=one).place(x=62,y=200)
tk.Button(root, text='2',width=4,fg='#28B463',font=('',24),command=two).place(x=142,y=200)
tk.Button(root, text='3',width=4,fg='#28B463',font=('',24),command=three).place(x=222,y=200)
tk.Button(root, text='x',width=4,fg='#28B463',font=('',24),command=prod).place(x=302,y=200)

#4to ROW
tk.Button(root, text='0',bd=0,width=4,fg='#28B463',font=('',24),command=zero).place(x=62,y=250)
tk.Button(root, text='=',width=4,fg='#28B463',font=('',24),command=resul).place(x=142,y=250)
tk.Button(root, text='-',width=4,fg='#28B463',font=('',24),command=resta).place(x=222,y=250)
tk.Button(root, text='+',width=4,fg='#28B463',font=('',24),command=suma).place(x=302,y=250)


root.mainloop()



