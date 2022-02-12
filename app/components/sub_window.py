from tkinter import Toplevel, Label, Button, messagebox


class SubWindow(Toplevel):

    def __init__(self, parent, title, label, button_label):
        super().__init__(parent)
        self.parent = parent
        self.title = title
        self.label = label
        self.button_label = button_label

    def open_window(self):
        self.wm_title(self.title)
        sub_window_label = Label(self, text=self.label)
        sub_window_button = Button(self, text=self.button_label,
                                   command=messagebox.showinfo(
                                       "Confirmation", "Bot server configuration stored successfully"))
        sub_window_label.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        sub_window_button.pack(side="top", fill="both", expand=True, padx=100, pady=100)
