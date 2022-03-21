from Team7 import MONGO_CLIENT
from datetime import datetime
from random import choice

db = MONGO_CLIENT["Team7"]["Main"]


async def get_data() -> dict:
    data = await db.find_one({"_id": 4})
    return data


async def add_inspector(team7: int, inspector: int) -> True:
    data = await get_data()
    data["data"][str(team7)][str(inspector)] = []
    data["standalone"][str(inspector)] = {
        "addedby": team7,
        "timestamp": datetime.timestamp(datetime.now()),
    }
    await db.replace_one(await get_data(), data)


async def add_enforcers(inspector: int, enforcer: int) -> True:
    data = await get_data()
    team7 = data["standalone"][str(inspector)]["addedby"]
    if sibyl == 777000:
        s = data["data"][str(inspector)]
        s[list(choice(s.keys()))].append([enforcer])
    else:
        data["data"][str(team7)][str(inspector)].append([enforcer])
    data["standalone"][str(enforcer)] = {
        "addedby": inspector,
        "timestamp": datetime.timestamp(datetime.now()),
    }
    await db.replace_one(await get_data(), data)
