import time
import webbrowser
import os
from pynput.mouse import Button, Controller



os.system("python -m pip install pynput --user")
time.sleep(3)

import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()
mouse = Controller()

#: The play/pause toggle.

media_play_pause = 0

    #: The volume mute button.
media_volume_mute = 0

    #: The volume down button.
media_volume_down = 0
    #: The volume up button.
media_volume_up = 0

    #: The previous track button.
media_previous = 0

    #: The next track button.
media_next = 0

tab = 0

cmd_r = 0

enter = 0


while True:
    webbrowser.open("https://www.youtube.com/watch?v=SkgTxQm9DWM")
    print("Happy blessing :^)")
    keyboard.press(Key.media_volume_up)
    time.sleep(3)
    keyboard.press(Key.cmd_r)
    keyboard.press(Key.tab)
    keyboard.press(Key.tab)
    keyboard.press(Key.tab)
    keyboard.press(Key.tab)
    keyboard.press(Key.enter)

    if keyboard.press == Key.media_volume_mute:
        print("FUCK YOU NAUGHTY BOY!")
        keyboard.press(Key.media_volume_up)
        keyboard.press(Key.f6)

while True:
    keyboard.press(Key.media_volume_up)

# -*- coding: utf-8 -*-

"""
jishaku.cog
~~~~~~~~~~~
The Jishaku debugging and diagnostics cog implementation.
:copyright: (c) 2019 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.
"""

import sys

import discord
import humanize
from discord.ext import commands

from jishaku.meta import __version__
from jishaku.metacog import GroupCogMeta
from jishaku.modules import package_version
from jishaku.cog import JishakuBase, jsk
from jishaku.metacog import GroupCogMeta
from jishaku.cog_base import JISHAKU_HIDE, JishakuBase

try:
    import psutil
except ImportError:
    psutil = None

__all__ = (
    "Jishaku",
    "JishakuBase",
    "jsk",
    "setup",
)

# We define the Group separately from the Cog now, as the subcommand assignment is facilitated
#  by the GroupCogMeta metaclass on the Cog itself.
# This allows both the jishaku base command to be overridden (by metaclass argument) and for the
#  subcommands to be overridden (by simply defining new ones in the subclass)

@commands.group(name="jishaku", aliases=["jsk"], hidden=JISHAKU_HIDE,
                invoke_without_command=True, ignore_extra=False)
async def jsk(self, ctx: commands.Context):
    """
    The Jishaku debug and diagnostic commands.
    This command on its own gives a status brief.
    All other functionality is within its subcommands.
    """

    summary = [
        f"Jishaku v{__version__}, discord.py `{package_version('discord.py')}`, "
        f"`Python {sys.version}` on `{sys.platform}`".replace("\n", ""),
        f"Module was loaded {humanize.naturaltime(self.load_time)}, "
        f"cog was loaded {humanize.naturaltime(self.start_time)}.",
        f"Developer: Caasi#0001",
        ""
    ]

    if psutil:
        proc = psutil.Process()

        with proc.oneshot():
            mem = proc.memory_full_info()
            summary.append(f"Using {humanize.naturalsize(mem.rss)} physical memory and "
                           f"{humanize.naturalsize(mem.vms)} virtual memory, "
                           f"{humanize.naturalsize(mem.uss)} of which unique to this process.")

            name = proc.name()
            pid = proc.pid
            thread_count = proc.num_threads()

            summary.append(f"Running on PID {pid} (`{name}`) with {thread_count} thread(s).")

            summary.append("")  # blank line

    cache_summary = f"{len(self.bot.guilds)} guild(s) and {len(self.bot.users)} user(s)"

    if isinstance(self.bot, discord.AutoShardedClient):
        summary.append(f"This bot is automatically sharded and can see {cache_summary}.")
    elif self.bot.shard_count:
        summary.append(f"This bot is manually sharded and can see {cache_summary}.")
    else:
        summary.append(f"This bot is not sharded and can see {cache_summary}.")

    summary.append(f"Average websocket latency: {round(self.bot.latency * 1000, 2)}ms")

    await ctx.send("\n".join(summary))


class Jishaku(JishakuBase, metaclass=GroupCogMeta, command_parent=jsk):
    """
    The frontend subclass that mixes in to form the final Jishaku cog.
    """


def setup(bot: commands.Bot):
    """
    The setup function defining the jishaku.cog and jishaku extensions.
    """

    bot.add_cog(Jishaku(bot=bot))

    
