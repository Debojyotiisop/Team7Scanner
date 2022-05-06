from Team7 import (
    System,
    system_cmd,
    make_collections,
    INSPECTORS,
    ENFORCERS,
    Sibyl_logs,
)
from telethon import TelegramClient, events, Button, types, functions, errors
from Team7.strings import on_string
import logging
import importlib
import asyncio
import time
from Team7 import SIBYL
from sys import version as ver
from telethon import version as vers
from Team7 import OWNERID

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

from Team7.plugins import to_load

HELP = {}
IMPORTED = {}
FAILED_TO_LOAD = {}

for load in to_load:
    try:
        imported = importlib.import_module("Team7.plugins." + load)
        if not hasattr(imported, "__plugin_name__"):
            imported.__plugin_name__ = imported.__name__

        if imported.__plugin_name__.lower() not in IMPORTED:
            IMPORTED[imported.__plugin_name__.lower()] = imported

        if hasattr(imported, "help_plus") and imported.help_plus:
            HELP[imported.__plugin_name__.lower()] = imported
    except Exception as e:
        print(f"Error while loading plugin: {load}")
        print("------------------------------------")
        print(e)
        FAILED_TO_LOAD[load] = e
        print("------------------------------------")


        
@System.on(system_cmd(pattern=r"t7info", allow_enforcer=True))
async def status(event):
    msg = await event.reply("ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ sᴇʀᴠᴇʀ ..")
    time.sleep(1)
    await msg.edit("ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ sᴇʀᴠᴇʀ ....")
    time.sleep(1)
    await msg.edit("ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ sᴇʀᴠᴇʀ ......")
    time.sleep(1)
    await msg.edit("ᴄᴏɴɴᴇᴄᴛɪᴏɴ sᴜᴄᴇssғᴜʟ !")
    time.sleep(1)
    await msg.edit("ʏᴏᴜ ᴀʀᴇ ᴀ ᴠᴇʀɪғɪᴇᴅ ᴜsᴇʀ")
    time.sleep(2)
    senderx = await event.get_sender()
    if event.sender.id in OWNERID:
        user_status = "**▪︎Owner▪︎**"
    elif event.sender.id in INSPECTORS:
        user_status = "**Inspector**"
    elif event.sender.id in SIBYL:
        User_status = "**Dev**"
    else: 
        user_status = "**Enforcer**"
    time.sleep(1)
    await msg.edit(on_string.format(Enforcer=user_status, name=senderx.first_name))

    
    
  

start_msg = """Hi {user}!
**Myself T7Scanner , mainly focused on working to reduce spam and scam .**
**__I can__**:
- __Auto detect illigal activity of telegram requests.__
- __Auto Push and release Watch From Gban System Requests.__
`Click the below button to know how to use me!`"""

@System.on(system_cmd(pattern=r"t7start", allow_slash=False, allow_inspectors=True))
async def send_help(event):
    from_ = await System.get_entity(event.sender_id)
    await event.reply(
        start_msg.format(user=from_.first_name),
        buttons=start_buttons,
        link_preview=False,
    )
    
    
    
    
@System.on(system_cmd(pattern="t7stats",allow_inspectors=True, allow_enforcer=True))
async def stats(event):
    msg = f"Processed {System.processed} messages since last restart."
    msg += f"\n{len(ENFORCERS)} Enforcers & {len(INSPECTORS)} Inspectors"
    g = 0
    async for d in event.client.iter_dialogs(limit=None):
        if d.is_channel and not d.entity.broadcast:
            g += 1
        elif d.is_group:
            g += 1
    msg += f"\nModerating {g} Groups"
    await event.reply(msg)


@System.on(system_cmd(pattern=r"t7help", allow_slash=False, allow_inspectors=True, allow_enforcer=True))
async def send_help(event):
    try:
        help_for = event.text.split(" ", 1)[1].lower()
    except IndexError:
        msg = "List of plugins with help text:\n"
        for x in HELP.keys():
            msg += f"`{x.capitalize()}`\n"
        await event.reply(msg)
        return
    if help_for in HELP:
        await event.reply(HELP[help_for].help_plus)
    else:
        return


async def main():
    try:
        await make_collections()
        me = await System.bot.get_me()
        System.bot.id = me.id
    except Exception as e:
        FAILED_TO_LOAD["main"] = e
    await System.start()
    await System.catch_up()
    if FAILED_TO_LOAD:
        msg = "Few plugins failed to load:"
        for plugin in FAILED_TO_LOAD:
            msg += f"\n**{plugin}**\n\n`{FAILED_TO_LOAD[plugin]}`"
        await System.send_message(Sibyl_logs, msg)
    else:
        await System.send_message(Sibyl_logs, "I am up!!")
    await System.run_until_disconnected()



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
