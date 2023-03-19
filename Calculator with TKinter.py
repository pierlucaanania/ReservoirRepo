'''GUI Calculator using TKinter'''

from tkinter import *

window = Tk()

window.title('Calculator')
window.geometry('400x400+75+100')

###

background_color_b = 'white'
write_color_b = 'black'

###

background_color = 'black'
write_color = 'yellow'

###

add1 = DoubleVar()
add2 = DoubleVar()
add3 = DoubleVar()

###

def sum():
    '''Summation of three numbers'''
    sumv = IntVar()
    sumv = (add1.get() + add2.get() + add3.get())
    text = Label(window, text = sumv, fg = write_color, bg = background_color, font = ('Helvetica',22)).pack()


def multiplication():
    '''Multiplication of three numbers'''
    sumv = IntVar()
    sumv = (add1.get() * add2.get() * add3.get())
    text = Label(window, text=sumv, fg=write_color, bg=background_color, font=('Helvetica', 22)).pack()


def divide():
    '''Division of three numbers'''
    sumv = IntVar()
    try:
        sumv = (add1.get() / add2.get() / add3.get())
        text = Label(window, text=sumv, fg=write_color, bg=background_color, font=('Helvetica', 22)).pack()
    except(ZeroDivisionError):
        text = Label(window, text = 'Ratio for 0!', fg=write_color, bg=background_color, font=('Helvetica', 22)).pack()

def subtract():
    '''Subtraction of three numbers'''
    sumv = IntVar()
    sumv = (add1.get() - add2.get() - add3.get())
    text = Label(window, text=sumv, fg=write_color, bg=background_color, font=('Helvetica', 22)).pack()

###

'''Entry'''

Add1 = Entry(window, textvariable=add1).pack(fill=X)
a = Label(text='***************************').pack(fill=X)
Add2 = Entry(window, textvariable=add2).pack(fill=X)
a = Label(text='***************************').pack(fill=X)
Add3 = Entry(window, textvariable=add3).pack(fill=X)

###

'''Button'''

Sum = Button(text='Sum', bg = background_color_b, fg = write_color_b, command=sum).pack(anchor=E, fill=X)
Mult = Button(text='Multiplication', bg = background_color_b, fg = write_color_b, command=multiplication).pack(anchor=E, fill=X)
Div = Button(text='Division', bg = background_color_b, fg = write_color_b, command=divide).pack(anchor=E, fill=X)
Subc = Button(text='Subtraction', bg = background_color_b, fg = write_color_b, command=subtract).pack(anchor=E, fill=X)

'''Mainloop'''

window.mainloop()