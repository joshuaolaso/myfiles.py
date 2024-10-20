import tkinter as tk
from math import sin, cos, tan, log, sqrt, pi, e

class ColorfulScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Colorful Scientific Calculator")

        self.entry = tk.Entry(master, width=40, borderwidth=5, bg='lightyellow', font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=5)

        self.create_buttons()

    def create_buttons(self):
        # Define button colors
        button_colors = {
            'default': 'lightblue',
            'operator': 'lightgreen',
            'function': 'lightcoral',
            'clear': 'salmon',
            'equal': 'lightgreen'
        }

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3, 'operator'), ('C', 1, 4, 'clear'),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3, 'operator'), ('sin', 2, 4, 'function'),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3, 'operator'), ('cos', 3, 4, 'function'),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2, 'operator'), ('=', 4, 3, 'equal'), ('tan', 4, 4, 'function'),
            ('log', 5, 0), ('sqrt', 5, 1), ('pi', 5, 2), ('e', 5, 3), ('^', 5, 4),
        ]

        for (text, row, col, *color_type) in buttons:
            color = button_colors.get(color_type[0], button_colors['default'])
            button = tk.Button(self.master, text=text, command=lambda t=text: self.on_button_click(t), bg=color, font=('Arial', 14))
            button.grid(row=row, column=col, sticky="nsew")

        # Configure grid weights for resizing
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif char in ['sin', 'cos', 'tan']:
            try:
                value = float(self.entry.get())
                if char == 'sin':
                    result = sin(value)
                elif char == 'cos':
                    result = cos(value)
                elif char == 'tan':
                    result = tan(value)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif char == 'log':
            try:
                value = float(self.entry.get())
                result = log(value)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif char == 'sqrt':
            try:
                value = float(self.entry.get())
                result = sqrt(value)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif char == 'pi':
            self.entry.insert(tk.END, pi)
        elif char == 'e':
            self.entry.insert(tk.END, e)
        elif char == '^':
            self.entry.insert(tk.END, '**')
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ColorfulScientificCalculator(root)
    root.mainloop()