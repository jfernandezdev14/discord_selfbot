from tkinter import Menu


class MenuBar(Menu):

    def __init__(self, parent, menu_bar_label):
        super().__init__(parent)
        self.parent = parent
        self.file_menu = Menu(self, tearoff=0)
        self.add_cascade(label=menu_bar_label, menu=self.file_menu)

    def add_menu_command(self, label, command_fn):

        pass


