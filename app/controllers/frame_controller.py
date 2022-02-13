import json
from tkinter import Label, Button, Toplevel, messagebox, Canvas, Entry, W, E

from app.components.frame_container import FrameContainer
from app.components.menu_bar import MenuBar
from app.components.tab_manager import TabManager


class FrameController(object):

    def __init__(self, root):
        self.root = root
        self.sub_window = None
        self.bot_name = None
        self.bot_token = None
        self.bot_proxy = None
        self.server_id = None

    def build_frame(self):
        self.root.title("Tab Widget")
        self.root.geometry("600x400")
        self.setup_menu_bar()
        tab_manager = TabManager(self.root)
        tab_1 = FrameContainer(tab_manager)
        tab_1.include_components()
        tab_manager.add_tab(tab_1, 'Primer Tab')
        tab_manager.pack()

    def setup_menu_bar(self):
        menu_bar = MenuBar(self.root, 'File')
        menu_bar.file_menu.add_command(label='Add Discord Bot', command=self.add_discord_bot)
        menu_bar.file_menu.add_command(label='Exit', command=self.root.quit)
        menu_bar.parent.config(menu=menu_bar)

    def add_discord_bot(self):
        self.sub_window = Toplevel(self.root)
        self.sub_window.geometry('600x120')
        self.sub_window.resizable(True, False)
        self.sub_window.wm_title('Add a new Discord Bot')

        # Define Add bot form
        Label(master=self.sub_window, text='Name your Bot').grid(row=0)
        bot_name = Entry(master=self.sub_window)
        bot_name.grid(row=0, column=1, sticky='ew')
        self.bot_name = bot_name
        Label(master=self.sub_window, text='Enter your Bot Token').grid(row=1)
        bot_token = Entry(master=self.sub_window)
        bot_token.grid(row=1, column=1, sticky='ew')
        self.bot_token = bot_token
        Label(master=self.sub_window, text='Enter your Bot Proxy (Optional)').grid(row=2)
        bot_proxy = Entry(master=self.sub_window)
        bot_proxy.grid(row=2, column=1, sticky='ew')
        self.bot_proxy = bot_proxy
        Label(master=self.sub_window, text='Enter Discord Server ID').grid(row=3)
        server_id = Entry(master=self.sub_window)
        server_id .grid(row=3, column=1, sticky='ew')
        self.server_id = server_id
        Button(self.sub_window, text='Connect Bot',
               command=self.add_bot_configuration).grid(row=4, columnspan=2)
        self.sub_window.columnconfigure(1, weight=1)
        self.sub_window.rowconfigure(4, weight=1)

    def add_bot_configuration(self):
        try:
            bot_configuration_file = open('./app/data/bots_configuration.json', 'r')
            bot_configuration = json.load(bot_configuration_file)
            bot_configuration_file.close()
            for account in bot_configuration['accounts']:
                if self.bot_name.get() == account['name']:
                    messagebox.showwarning(
                        "Alert", "Bot server configuration already exists.")
                    self.sub_window.destroy()
                    raise

            new_bot_configuration = {
                "name": self.bot_name,
                "token": self.bot_token,
                "proxy": self.bot_proxy,
                "user_id": None,
                "channelIDs_time": None,
                "file_contaning_message": None
            }

            bot_configuration_file = open('./app/data/bots_configuration.json', 'w')
            json.dump(bot_configuration, bot_configuration_file)
            bot_configuration_file.close()
            self.bot_creation_success_message()

        except Exception as e:
            print("Bot configuration file is corrupted or doesn't exist. " + e)

    def bot_creation_success_message(self):
        messagebox.showinfo(
            "Confirmation", "Bot server configuration stored successfully")
        self.sub_window.destroy()
