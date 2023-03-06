from tkinter import END


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


def equation_button(entry, equation_sign, num_1, new_num, equation):
    new_num.set(True)
    num_1.set(entry.get())
    equation_sign.set(equation)
    new_num.set(True)


def egual_cal(entry, equation_sign, num_1, new_num):
    x = int(num_1.get())
    y = int(entry.get())
    if equation_sign.get() == '+':
        entry.delete(0, END)
        entry.insert(0, x + y)
    elif equation_sign.get() == '-':
        entry.delete(0, END)
        entry.insert(0, x - y)
    if equation_sign.get() == '*':
        entry.delete(0, END)
        entry.insert(0, x * y)
    elif equation_sign.get() == '/':
        entry.delete(0, END)
        if y == 0:
            entry.insert(0, 'ERR')
        else:
            entry.insert(0, x / y)
    new_num.set(True)


def clear_cal(entry):
    entry.delete(0, END)
    entry.insert(0, '0')
