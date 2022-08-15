import tkinter as tk
from discord.ext import commands
from threading import Thread

from app.constants import DISCORD_BOT_TOKEN
from app.controllers.frame_controller import FrameController


def start_discord_bot():
    bot = commands.Bot(command_prefix='_', description="I am DevBot")
    bot.load_extension('app.controllers.discord_bot_controller')
    bot.run(DISCORD_BOT_TOKEN)


def start_frame_thread():
    root = tk.Tk()
    frame_controller = FrameController(root)
    frame_controller.build_frame()
    root.mainloop()


def main():

    tk_thread = Thread(
        target=start_frame_thread, args=[]
    )
    tk_thread.start()
    # start_discord_bot()


main()
