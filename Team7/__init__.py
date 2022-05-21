"""Gets ENV vars or Config vars then calls class."""


from telethon import events
from telethon.sessions import StringSession
from motor import motor_asyncio
import aiohttp
import json
from datetime import datetime
from pyrogram import Client
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
import asyncio
import traceback
import logging
import os
import re

if os.path.exists('log.txt'):
    os.remove("log.txt")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)


API_ID_KEY = 19153657
API_HASH_KEY = "f7ec417477c60578119d3d0bcf42f38c"
STRING_SESSION = "1BVtsOK4Bu7_48BNrPO3Zaee9GSk8nQI0Ii9X6q0aEzbZF1XSv9AA5iquVWtvBJXLrNgFjuVnR768s-UWuoOyye927ii9ir6FB9nO-qJqa0JuhZipgSb0EMfrcLDE6BwpGb4NWT__5GynoHde0tiBH5NzwxUE5ESPb7c2MKvQzDExTZU9vrGGUBEpSSK9Ri-b_DE5244rgRqm0flCl4x4T0EnNSsZHkIO0Px0hEcS08W5Yhacp3nViu5KCMrqi_72a0jY7sdE_Mykd9S24IR1DS6GKgtLvOVPrzhYN8MXWtU7vr99KIdT2mWGiKR_Z5o-bXhFVAEmTL2QmOXTMNlFQhBhwLD4udc="
MONGO_DB_URL = "mongodb+srv://scan:scan123@scanner.xxtiq.mongodb.net/?retryWrites=true&w=majority"
SIBYL = [2093473332,5146000168]
ENFORCERS = [2093473332,5146000168]
INSPECTORS = [1537076718,5001573230,2070119160,5069705982,5147265129,1242979521,2131857711,5213143273,837914403,1608911105,5278295844,1883976677,998589443,1789859817,5292346355]
Sibyl_logs = (-1001525807961)
Sibyl_approved_logs = (-1001525807961)
GBAN_MSG_LOGS = (-1001525132581)
BOT_TOKEN = "5394211831:AAEQEU_doh1wqoxT5i1cq9N3tfsGTJHpiSY"
OWNERID = [2093473332,5146000168]

INSPECTORS.extend(SIBYL)
ENFORCERS.extend(INSPECTORS)
OWNERID.extend(OWNERID)

session = aiohttp.ClientSession()

MONGO_CLIENT = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)

from .client_class import SibylClient

try:
    System = SibylClient(StringSession(STRING_SESSION), API_ID_KEY, API_HASH_KEY)
except:
    print(traceback.format_exc())
    exit(1)

collection = MONGO_CLIENT["Sibyl"]["Main"]


pbot = Client(

    ":memory:",

    api_id=API_ID_KEY,

    api_hash=API_HASH_KEY,

    bot_token=BOT_TOKEN,

    workers=min(32, os.cpu_count() + 4),

)

apps = []

apps.append(pbot)

loop = asyncio.get_event_loop()


async def make_collections() -> str:
    if (
        await collection.count_documents({"_id": 1}, limit=1) == 0
    ):  # Blacklisted words list
        dictw = {'_id': 1, 'blacklisted': []}
        await collection.insert_one(dictw)

    if (
        await collection.count_documents({"_id": 2}, limit=1) == 0
    ):  # Blacklisted words in name list
        dictw = {'_id': 2, 'Type': 'Wlc Blacklist', 'blacklisted_wlc': []}
        await collection.insert_one(dictw)
    if await collection.count_documents({"_id": 3}, limit=1) == 0:  # Gbanned users list
        dictw = {
            '_id': 3,
            'Type': 'Gban:List',
            'victim': [],
            'gbanners': [],
            'reason': [],
            'proof_id': [],
        }

        await collection.insert_one(dictw)
    if await collection.count_documents({"_id": 4}, limit=1) == 0:  # Rank tree list
        sample_dict = {'_id': 4, 'standalone': {}, 'data': {}}
        for x in SIBYL:
            sample_dict["data"][str(x)] = {}
            sample_dict["standalone"][str(x)] = {
                "added_by": 777000,
                "timestamp": datetime.timestamp(datetime.now()),
            }
        await collection.insert_one(sample_dict)
    return ""


def system_cmd(
    pattern=None,
    allow_sibyl=True,
    allow_enforcer=False,
    allow_inspectors=False,
    allow_slash=True,
    force_reply=False,
    **args
):
    if pattern and allow_slash:
        args["pattern"] = re.compile(r"[\?\.!/](" + pattern + r")(?!@)")
    else:
        args["pattern"] = re.compile(r"[\?\.!]" + pattern)
    if allow_sibyl and allow_enforcer:
        args["from_users"] = ENFORCERS
    elif allow_inspectors and allow_sibyl:
        args["from_users"] = INSPECTORS
    else:
        args["from_users"] = SIBYL
    if force_reply:
        args["func"] = lambda e: e.is_reply
    return events.NewMessage(**args)
