from ttkbootstrap import Window, Style, Button
from tkinter import DoubleVar, StringVar, BooleanVar, Entry
from functions import *

# Inicjalizacja głównego okna aplikacji z Tkbootstrap
root = Window(title="Calculator", themename="flatly", resizable=(False, False))
root.title("Calculator")

# Tworzenie pola wejściowego do wyświetlania i wprowadzania liczb
e = Entry(root, width=35, borderwidth=5, justify='right')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
e.insert(0, "0")

# Lista przycisków
buttons = []

# Zmienne globalne do przechowywania pierwszej liczby, znaku równości i flagi nowej liczby
temp_num1 = DoubleVar()
equal_sign = StringVar()
new_number = BooleanVar()
new_number.set(False)

# Funkcja do tworzenia przycisków numerycznych
for i in range(9, 0, -1):
    btn_number = Button(text=str(i), width=10,
                             command=lambda entry=e, number=i, new_num=new_number: number_button(entry,
                                                                                                 number, new_num))
    btn_number.grid(column=(i+2) % 3 + 1, row=((9-i) // 3) + 1)
    buttons.append(btn_number)

# Tworzenie przycisku dla liczby 0
btn_number_zero = Button(text='0', width=10,
                              command=lambda entry=e, number='0', new_num=new_number: number_button(entry,
                                                                                                    number, new_num))
btn_number_zero.grid(column=1, row=4)

# Tworzenie przycisków dla operatorów matematycznych
equations = ['+', '-', '*', '/']
for idx, equation in enumerate(equations):
    btn_number = Button(
        text=equation, width=10,
        command=lambda entry=e, eq_sign=equal_sign, num_1=temp_num1, new_num=new_number, eq=equation:
        equation_button(entry, eq_sign, num_1, new_num, eq))
    btn_number.grid(column=0, row=idx+1)
    buttons.append(btn_number)

# Tworzenie przycisku równości
btn_equal = Button(text="=", width=10,
                        command=lambda entry=e, eq_sign=equal_sign, num_1=temp_num1, new_num=new_number:
                        egual_cal(entry, eq_sign, num_1, new_num))
btn_equal.grid(column=3, row=4)

# Tworzenie przycisku czyszczenia
btn_clear = Button(text="C", width=10, command=lambda entry=e: clear_cal(entry))
btn_clear.grid(column=2, row=4)

# Uruchomienie głównej pętli aplikacji
root.mainloop()
