import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("800x800")
        self.root.configure(bg='black')

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Scientific Calculator", font=("Arial", 30, "bold"), bg='black', fg='white')
        title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Container for calculator UI
        container = tk.Frame(self.root, bg='white', relief=tk.RAISED, bd=2)
        container.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=500, height=700)

        entry = ttk.Entry(container, textvariable=self.result_var, font=("Arial", 24, "bold"), justify='right')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('%', 5, 3),
            ('^', 6, 0), ('√', 6, 1), ('mod', 6, 2), ('e', 6, 3),
            ('C', 7, 0), ('(', 7, 1), (')', 7, 2), ('deg', 7, 3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(container, text=text, command=lambda t=text: self.on_button_click(t), style="Custom.TButton")
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

        for i in range(8):
            container.grid_rowconfigure(i, weight=1)
        for j in range(4):
            container.grid_columnconfigure(j, weight=1)

        # Apply styles
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 14, "bold"), padding=10)

    def on_button_click(self, char):
        try:
            if char == '=':
                expression = self.result_var.get()
                # Handle square root and trigonometric functions
                expression = expression.replace('√', 'math.sqrt').replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan').replace('deg', 'math.degrees').replace('rad', 'math.radians')
                result = eval(expression.replace('^', '**').replace('mod', '%'))
                self.result_var.set(result)
            elif char == 'C':
                self.result_var.set("0")
            else:
                current_text = self.result_var.get()
                if current_text == "0":
                    self.result_var.set(char)
                else:
                    self.result_var.set(current_text + char)
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
