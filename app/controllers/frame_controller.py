import json
from tkinter import Label, Button, Toplevel, messagebox, Canvas, Entry, W, E, Listbox, Scrollbar
from tkinter.constants import RIGHT, BOTH

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
        self.bot_manager_tab = None
        self.bot_configuration_tab = None
        self.manager_tab_bot_list = None
        self.manager_tab_active_bot_list = None

    def build_frame(self):
        self.root.title("Discord SelfBot Manager")
        self.root.geometry("600x400")
        self.setup_menu_bar()
        tab_manager = TabManager(self.root)
        self.bot_manager_tab = FrameContainer(tab_manager)
        tab_manager.add_tab(self.bot_manager_tab, 'Bot Manager')
        tab_manager.pack()
        self.setup_bot_manager_tab()
        self.bot_configuration_tab = FrameContainer(tab_manager)
        self.bot_configuration_tab.include_components()
        tab_manager.add_tab(self.bot_configuration_tab, 'Bot Configuration')
        tab_manager.pack()

    def setup_bot_manager_tab(self):

        # Define Registered bot list
        Label(master=self.bot_manager_tab, text='Registered Bots').grid(row=0, column=0)
        Label(master=self.bot_manager_tab, text='Active Bots').grid(row=0, column=6)
        self.manager_tab_bot_list = Listbox(self.bot_manager_tab)
        scrollbar_manager_bot_list = Scrollbar(self.bot_manager_tab)
        scrollbar_manager_bot_list.grid(row=1, column=1, rowspan=6, sticky='w')
        self.manager_tab_bot_list.config(yscrollcommand=scrollbar_manager_bot_list.set)
        scrollbar_manager_bot_list.config(command=self.manager_tab_bot_list.yview)

        try:
            bot_configuration_file = open('./app/data/bots_configuration.json', 'r')
            bot_configuration = json.load(bot_configuration_file)
            bot_configuration_file.close()
            if 'accounts' in bot_configuration:
                i = 1
                for account in bot_configuration['accounts']:
                    self.manager_tab_bot_list.insert(i, account['name'])
                    i = i + 1

        except Exception as e:
            print("Bot configuration file is corrupted or doesn't exist. Failed loading existing bots" + e)
        self.manager_tab_bot_list.grid(row=1, rowspan=6, column=0, sticky='nws')

        # Define buttons to activate the bots
        activate_bot_button = Button(master=self.bot_manager_tab, text='Activate Bot >>', command=None)
        activate_bot_button.grid(row=2, column=2)
        activate_all_bots_button = Button(master=self.bot_manager_tab, text='Activate all >>', command=None)
        activate_all_bots_button.grid(row=3, column=2)
        deactivate_bot_button = Button(master=self.bot_manager_tab, text='<< Deactivate Bot', command=None)
        deactivate_bot_button.grid(row=4, column=2)
        deactivate_all_bots_button = Button(master=self.bot_manager_tab, text='<< Deactivate all', command=None)
        deactivate_all_bots_button.grid(row=5, column=2)

        # Define active bots list
        self.manager_tab_active_bot_list = Listbox(self.bot_manager_tab)
        self.manager_tab_active_bot_list.grid(row=1, rowspan=6, column=6, sticky='nes')

        self.bot_manager_tab.columnconfigure(1, weight=1)
        self.bot_manager_tab.rowconfigure(1, weight=1)
        self.bot_manager_tab.rowconfigure(2, weight=1)
        self.bot_manager_tab.rowconfigure(3, weight=1)
        self.bot_manager_tab.rowconfigure(4, weight=1)
        self.bot_manager_tab.rowconfigure(5, weight=1)
        self.bot_manager_tab.rowconfigure(6, weight=1)

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
        server_id.grid(row=3, column=1, sticky='ew')
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
                "name": self.bot_name.get(),
                "token": self.bot_token.get(),
                "proxy": self.bot_proxy.get(),
                "user_id": None,
                "channelIDs_time": None,
                "file_contaning_message": None
            }
            bot_configuration['accounts'].append(new_bot_configuration)

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
