import json
from tkinter import filedialog, StringVar


def open_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Open file", filetypes=(("Json files", "*.json"),))
    if file_path:
        StringVar().set(file_path)
        file = open(file_path, 'r')
        data = json.load(file)
        file.close()




def save_file():
    print(filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                       filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))
