from tkinter import *
from functions import *

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

for i in range(9, 0, -1):
    btn_number = Button(root, text=str(i), padx=40, pady=20,
                        command=lambda entry=e, number=i, new_num=new_num: number_button(entry, number, new_num))

    btn_number.grid(column=(i+2) % 3, row=((9-i) // 3) + 1)
    buttons.append(btn_number)
btn_number_zero = Button(root, text='0', padx=88, pady=20,
                         command=lambda entry=e, number='0', new_num=new_num: number_button(entry, number, new_num))
btn_number_zero.grid(column=0, row=4, columnspan=2)
equations = ['+', '-', '*', '/']
for idx, equation in enumerate(equations):
    btn_number = Button(root, text=equation, padx=39 if idx == 0 else 40, pady=20,
                        command=lambda entry=e, eq_sign=eq_sign, num_1=temp_num1, new_num=new_num, equation=equation:
                        equation_button(entry, eq_sign, num_1, new_num, equation))
    btn_number.grid(column=(14 + idx) % 3, row=((11+idx) // 3) + 1)
    buttons.append(btn_number)

btn_equal = Button(root, text="=", padx=91, pady=20,
                   command=lambda entry=e, eq_sign=eq_sign, num_1=temp_num1, new_num=new_num:
                   egual_cal(entry, eq_sign, num_1, new_num))
btn_clear = Button(root, text="C", padx=38, pady=20, command=lambda entry=e: clear_cal(entry))
btn_clear.grid(column=0, row=6)
btn_equal.grid(column=1, row=6, columnspan=2)

root.mainloop()