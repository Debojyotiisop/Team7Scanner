import re
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from Team7 import System, ENFORCERS, INSPECTORS, SIBYL

def team7_system_cmd(
    pattern=None,
    allow_Skynet=True,
    allow_enforcer=False,
    allow_inspectors=False,
    allow_slash=True,
    force_reply=False,
    **args
):
    if pattern and allow_slash:
#        args["pattern"] = re.compile(r"[\?\.!/](" + pattern + r")(?!@)")
        args["pattern"] = re.compile(r"[\?\.!/]" + pattern)
    else:
        args["pattern"] = re.compile(r"[\?\.!]" + pattern)
    if allow_Skynet and allow_enforcer:
        args["from_users"] = ENFORCERS
    elif allow_inspectors and allow_Skynet:
        args["from_users"] = INSPECTORS
    else:
        args["from_users"] = SIBYL
    if force_reply:
        args["func"] = lambda e: e.is_reply
    return events.NewMessage(**args)


@System.on(team7_system_cmd(pattern=r"info"))
async def whois(event):
    try:
        to_get = event.pattern_match.group(1)
    except Exception:
        if event.reply:
            replied = await event.get_reply_message()
            to_get = int(replied.sender.id)
        else:
            return
    try:
        to_get = int(to_get)
    except Exception:
        pass
    try:
        data = await System(GetFullUserRequest(to_get))
    except Exception:
        await event.reply("Failed to get data of the user")
        return
    await System.send_message(
        event.chat_id,
        f"Perma Link: [{data.user.first_name}](tg://user?id={data.user.id})\nUser ID: `{data.user.id}`\nAbout: {data.about}",
    )


help_plus = """ Here is Help for **Whois** -
`whois` - get data of the user
**Notes:**
`/` `?` `.` `!` are supported prefixes.
**Example:** `/addenf` or `?addenf` or `.addenf`
"""
__plugin_name__ = "Info"
