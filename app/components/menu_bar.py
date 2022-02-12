from tkinter import Menu


class MenuBar(Menu):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.file_menu = Menu(self, tearoff=0)

    def add_menu_command(self, label, command_fn):

        self.file_menu.add_command(label=label, command=command_fn)
        self.add_cascade(label="File", menu=self.file_menu)
        self.parent.config(menu=self)


