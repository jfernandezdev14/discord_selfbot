from tkinter.ttk import Label, Button, Frame


class FrameContainer(Frame):

    def __init__(self, parent):
        super().__init__(parent, padding=10)

    def include_components(self):
        Label(self, text="Hello World!").grid(column=0, row=0)

