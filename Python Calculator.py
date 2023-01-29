import tkinter as tk

def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operator = operator_entry.get()

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "Invalid operator"

    result_label.config(text=result)

root = tk.Tk()
root.title("Calculator")

num1_label = tk.Label(root, text="Number 1")
num1_label.grid(row=0, column=0)

num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1)

num2_label = tk.Label(root, text="Number 2")
num2_label.grid(row=1, column=0)

num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1)

operator_label = tk.Label(root, text="Operator")
operator_label.grid(row=2, column=0)

operator_entry = tk.Entry(root)
operator_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
