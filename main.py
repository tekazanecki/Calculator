from tkinter import *


def number_button(entry, number, new_num):
    if new_num.get():
        entry.delete(0, END)
        entry.insert(0, number)
    else:
        if entry.get() == '0':
            entry.delete(0, END)
            entry.insert(0, number)
        else:
            entry.insert(END, number)
    new_num.set(False)

def adding_cal(entry, equasion_sign, num_1, new_num):
    new_num.set(True)
    num_1.set(entry.get())
    equasion_sign.set('+')
    new_num.set(True)

def egual_cal(entry, equasion_sign, num_1):
    x = int(num_1.get())
    y = int(entry.get())
    if equasion_sign.get() == '+':
        entry.delete(0, END)
        entry.insert(0, x+y)
    new_num.set(True)
def clear_cal(entry,):
    entry.delete(0, END)
    entry.insert(0, '0')


root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5,justify=RIGHT)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, "0")

buttons = []
temp_num1 = DoubleVar()
eq_sign = StringVar()
new_num = BooleanVar()
new_num.set(False)

for i in range(10):
    btn_number = Button(root, text=str(i), padx=40, pady=20,
                        command=lambda entry=e, number=i, new_num=new_num: number_button(entry, number, new_num))
    btn_number.grid(column=i % 3, row=(i // 3) + 1)
    buttons.append(btn_number)
btn_add = Button(root, text="+", padx=39, pady=20,
                 command=lambda entry=e, eq_sign=eq_sign, num_1=temp_num1, new_num=new_num:
                 adding_cal(entry, eq_sign, num_1, new_num))
btn_equal = Button(root, text="=", padx=91, pady=20,
                   command=lambda entry=e, eq_sign=eq_sign, num_1=temp_num1: egual_cal(entry, eq_sign, num_1))
btn_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda entry=e, number=i: clear_cal(entry))
btn_add.grid(column=0, row=5)
btn_equal.grid(column=1, row=5, columnspan=2)
btn_clear.grid(column=1, row=4, columnspan=2)



root.mainloop()