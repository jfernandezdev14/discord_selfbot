from tkinter.ttk import Notebook


class TabManager(Notebook):

    def __init__(self, parent):
        super().__init__(parent, padding=10)

    def add_tab(self, new_tab, tab_name):
        self.add(new_tab, text=tab_name)
        self.pack(expand=1, fill="both")
