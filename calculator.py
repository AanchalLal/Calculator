from tkinter import *
expr=" "
def btnclk(n):
    global expr
    expr=expr+str(n)
    v.set(expr)
def calculate():
    global expr
    result=eval(expr)
    v.set(result)
def clear():
    global expr
    expr=" "
    v.set(expr)

w=Tk()
v=StringVar()
w.title("CALCULATOR")
#design all components
E=Entry(w,textvariable=v,justify='right',bg='cyan',font=('arial',15,'bold'),bd=5)
B1=Button(w,text="1",font=('arial',15,'bold'),command=lambda:btnclk(1),bg='pink')
B2=Button(w,text="2",font=('arial',15,'bold'),command=lambda:btnclk(2),bg='pink')
B3=Button(w,text="3",font=('arial',15,'bold'),command=lambda:btnclk(3),bg='pink')
B4=Button(w,text="4",font=('arial',15,'bold'),command=lambda:btnclk(4),bg='pink')
B5=Button(w,text="5",font=('arial',15,'bold'),command=lambda:btnclk(5),bg='pink')
B6=Button(w,text="6",font=('arial',15,'bold'),command=lambda:btnclk(6),bg='pink')
B7=Button(w,text="7",font=('arial',15,'bold'),command=lambda:btnclk(7),bg='pink')
B8=Button(w,text="8",font=('arial',15,'bold'),command=lambda:btnclk(8),bg='pink')
B9=Button(w,text="9",font=('arial',15,'bold'),command=lambda:btnclk(9),bg='pink')
B0=Button(w,text="0",font=('arial',15,'bold'),command=lambda:btnclk(0),bg='pink')
Bequal=Button(w,text="=",font=('arial',15,'bold'),command=lambda:calculate(),bg='pink')
Bclear=Button(w,text="c",font=('arial',15,'bold'),command=lambda:clear(),bg='pink')
Bplus=Button(w,text="+",font=('arial',15,'bold'),command=lambda:btnclk('+'),bg='pink')
Bminus=Button(w,text="-",font=('arial',15,'bold'),command=lambda:btnclk('-'),bg='pink')
Bmul=Button(w,text="*",font=('arial',15,'bold'),command=lambda:btnclk('*'),bg='pink')
Bdiv=Button(w,text="/",font=('arial',15,'bold'),command=lambda:btnclk('/'),bg='pink')
#place the components 
#row 1
E.grid(row=1,column=1,columnspan=4)
#row 2
B1.grid(row=2,column=1)
B2.grid(row=2,column=2)
B3.grid(row=2,column=3)
B4.grid(row=2,column=4)
#row 3
B5.grid(row=3,column=1)
B6.grid(row=3,column=2)
B7.grid(row=3,column=3)
B8.grid(row=3,column=4)
#row 4
B9.grid(row=4,column=1)
B0.grid(row=4,column=2)
Bequal.grid(row=4,column=3)
Bclear.grid(row=4,column=4)
#row 5
Bplus.grid(row=5,column=1)
Bminus.grid(row=5,column=2)
Bmul.grid(row=5,column=3)
Bdiv.grid(row=5,column=4)
#
