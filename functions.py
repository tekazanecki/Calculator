from tkinter import END

# Function to handle number button press
def number_button(entry, number, new_num):
    """
    Handle the event when a number button is pressed.

    Args:
        entry: The entry widget where the number will be displayed.
        number: The number that was pressed.
        new_num: A BooleanVar indicating whether a new number is being entered.
    """
    # If a new number is being entered, clear the entry field and insert the number
    if new_num.get():
        entry.delete(0, END)
        entry.insert(0, number)
    else:
        # If the current entry is '0', replace it with the new number
        if entry.get() == '0':
            entry.delete(0, END)
            entry.insert(0, number)
        else:
            # Otherwise, append the number to the current entry
            entry.insert(END, number)
    new_num.set(False)

# Function to handle operator button press
def equation_button(entry, equation_sign, old_num, new_num, equation):
    """
    Handle the event when an operator button is pressed.

    Args:
        entry: The entry widget where the number is displayed.
        equation_sign: A StringVar to store the selected operator.
        old_num: A DoubleVar to store the first number.
        new_num: A BooleanVar indicating whether a new number is being entered.
        equation: The selected operator (+, -, *, /).
    """
    # Set the flag for new number, store the current number and the chosen operator
    new_num.set(True)
    old_num.set(entry.get())
    equation_sign.set(equation)
    new_num.set(True)

# Function to handle the equal button press and perform the calculation
def equal_cal(entry, equation_sign, old_num, new_num):
    """
    Handle the event when the equal button is pressed and perform the calculation.

    Args:
        entry: The entry widget where the result will be displayed.
        equation_sign: A StringVar storing the selected operator.
        old_num: A DoubleVar storing the first number.
        new_num: A BooleanVar indicating whether a new number is being entered.
    """
    x = int(old_num.get())
    y = int(entry.get())
    # Perform the calculation based on the chosen operator and update the entry field
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

# Function to clear the calculator entry field
def clear_cal(entry):
    """
    Clear the calculator entry field and reset it to '0'.

    Args:
        entry: The entry widget to be cleared.
    """
    entry.delete(0, END)
    entry.insert(0, '0')
