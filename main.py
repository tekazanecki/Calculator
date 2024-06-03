from ttkbootstrap import Window, Style, Button
from tkinter import DoubleVar, StringVar, BooleanVar, Entry
from functions import *

class Calculator:
    def __init__(self, root):
        """
        Initialize the main application window and its components.
        """
        self.root = root
        self.root.title("Calculator")
        self.style = Style()
        self.style.theme_use('flatly')  # You can change the theme to any available in ttkbootstrap

        # Create an input field for displaying and entering numbers
        self.entry = Entry(self.root, width=35, borderwidth=5, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.entry.insert(0, "0")

        # Global variables to store the first number, the equal sign, and the new number flag
        self.temp_num = DoubleVar()
        self.equal_sign = StringVar()
        self.new_number = BooleanVar()
        self.new_number.set(False)

        # Create numeric buttons
        self.create_number_buttons()

        # Create a button for the number 0
        self.create_zero_button()

        # Create buttons for mathematical operators
        self.create_operator_buttons()

        # Create the equal sign button
        self.create_equal_button()

        # Create the clear button
        self.create_clear_button()

    def create_number_buttons(self):
        """
        Create buttons for numbers 1 to 9.
        """
        for i in range(9, 0, -1):
            btn_number = Button(text=str(i), width=10,
                                command=lambda number=i: number_button(self.entry, number, self.new_number))
            btn_number.grid(column=(i + 2) % 3 + 1, row=((9 - i) // 3) + 1)

    def create_zero_button(self):
        """
        Create a button for the number 0.
        """
        btn_number_zero = Button(text='0', width=10,
                                 command=lambda: number_button(self.entry, '0', self.new_number))
        btn_number_zero.grid(column=1, row=4)

    def create_operator_buttons(self):
        """
        Create buttons for mathematical operators.
        """
        equations = ['+', '-', '*', '/']
        for idx, equation in enumerate(equations):
            btn_operator = Button(
                text=equation, width=10,
                command=lambda eq=equation: equation_button(self.entry, self.equal_sign, self.temp_num, self.new_number, eq))
            btn_operator.grid(column=0, row=idx + 1)

    def create_equal_button(self):
        """
        Create the equal sign button.
        """
        btn_equal = Button(text="=", width=10,
                           command=lambda: equal_cal(self.entry, self.equal_sign, self.temp_num, self.new_number))
        btn_equal.grid(column=3, row=4)

    def create_clear_button(self):
        """
        Create the clear button.
        """
        btn_clear = Button(text="C", width=10, command=lambda: clear_cal(self.entry))
        btn_clear.grid(column=2, row=4)

if __name__ == "__main__":
    root = Window(title="Calculator", themename="flatly", resizable=(False, False))
    app = Calculator(root)
    root.mainloop()