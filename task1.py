import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os

class FileManager:
    def __init__(self, master):
        self.master = master
        master.title("Simple File Manager")

        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        self.open_button = tk.Button(self.frame, text="Open File", command=self.open_file)
        self.open_button.pack(side=tk.LEFT)

        self.list_button = tk.Button(self.frame, text="List Files", command=self.list_files)
        self.list_button.pack(side=tk.LEFT)

        self.text_area = Text(master, width=60, height=20, wrap=tk.NONE)
        self.text_area.pack(pady=10)

        self.scrollbar = tk.Scrollbar(master, command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def list_files(self):
        directory = filedialog.askdirectory()
        if directory:
            try:
                files = os.listdir(directory)
                self.text_area.delete(1.0, tk.END)
                for file in files:
                    self.text_area.insert(tk.END, file + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"Could not list files: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    file_manager = FileManager(root)
    root.mainloop()