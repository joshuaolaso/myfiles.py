import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=5)

        # Define buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sin', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('cos', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('tan', 4, 4),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Configure grid weights for resizing
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif char in ['sin', 'cos', 'tan']:
            try:
                value = float(self.display.get())
                if char == 'sin':
                    result = math.sin(math.radians(value))
                elif char == 'cos':
                    result = math.cos(math.radians(value))
                elif char == 'tan':
                    result = math.tan(math.radians(value))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()