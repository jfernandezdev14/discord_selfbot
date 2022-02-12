
from app.components.frame_container import FrameContainer
from app.components.menu_bar import MenuBar
from app.components.sub_window import SubWindow
from app.components.tab_manager import TabManager


class FrameController(object):

    @staticmethod
    def build_frame(root):
        root.title("Tab Widget")
        root.geometry("600x400")
        setup_menu_bar(root)
        tab_manager = TabManager(root)
        tab_1 = FrameContainer(tab_manager)
        tab_1.include_components()
        tab_manager.add_tab(tab_1, 'Primer Tab')
        tab_manager.pack()


def setup_menu_bar(root):
    menu_bar = MenuBar(root)
    menu_bar.add_menu_command('Add Discord Bot', add_discord_bot(root))
    menu_bar.add_menu_command('Exit', root.quit)


def add_discord_bot(parent):
    SubWindow(parent, 'Add a new Discord Bot', 'Hello', 'Connect Bot')
