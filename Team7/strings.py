on_string = """
「 ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴛᴇᴀᴍ 7 」
➖➖➖➖➖➖➖➖➖➖➖➖➖
• ɴᴀᴍᴇ : ㅤYASH
• ʀᴀɴᴋ : Inspector
➖➖➖➖➖➖➖➖➖➖➖➖➖
「 ʏᴏᴜ ᴀʀᴇ ᴀɴ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀ ! 」
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
$SCAN
Cymatic Scan request!
**Enforcer:** {enforcer}
**User scanned:** {spammer}
**Reason:** `{reason}`
**Scan Source:** {chat}
**Target Message:** `{message}`
"""
forced_scan_string = """
$FORCED
**Inspector:** {ins}
**Target:** {spammer}
**Reason:** `{reason}`
**Scan Source:** {chat}
**Target Message:** `{message}`
"""

group_admin_scan_string = """
$ENFORCED CHAT-BAN
**Inspector**: {ins}
*Target**: {t_chat}
**Reason**: `{reason}`
**ʀᴏᴏᴛ**: {chat}
**Chat Owner**: 
`{owner_id}`
**Admins**: `{admins}`
"""
group_admin_request_string = """
$CHAT-BAN
Group Ban Request!
*Inspector**: {enf}
**Target**: {t_chat}
**Reason**: `{reason}`
***Link**: {chat}
**Chat Owner**: 
`{owner_id}`
**Admins**: `{admins}`
"""

revert_request_string = """
$UNSCAN
Unban request!
**Inspector:** `{enforcer}`
**UNSCAN USER:** `{spammer}`
**ORGINATED:** {chat}
"""

revert_reject_string = """
$DECLINED
**SCANNED:** `Request declined`
SCAn Request delicned by {ins}, HEad to [Team7](http://t.me/Tg_power_fed_007).
"""

reject_string = """
$DECLINED
**SCAN ** `REquest declined`
Scaned Request delicned by {ins}, HEad to [Team7](http://t.me/Tg_power_fed_007).
"""

proof_string = """
**Case file for** - {proof_id} :
┣━**Reason**: {reason}
┗━**Message**
         ┣━[Nekobin]({paste})
         ┗━[DelDog]({url})"""


scan_approved_string = """
「 SCAN RESULT 」
**Tᴀʀɢᴇᴛ:** {scam}
**Cʀɪᴍᴇ Stats:** `Over 300`
**Rᴇᴀsᴏɴ:** `{reason}`
**Enforcer:** `{enforcer}`
**Cᴀsᴇ Nᴜᴍʙᴇʀ:** `{proof_id}`
"""

bot_gban_string = """
#DestroyDecomposer
**Enforcer:** `{enforcer}`
**Target User:** {scam}
**Reason:** `{reason}`
"""

report_by_user = """
**Report By User**
**Inspector:** {exu}
**Target:** {userr}
**Reason:** {reasonn}
**Reason By User:** {reason}
"""
# https://psychopass.fandom.com/wiki/Crime_Coefficient_(Index)
# https://psychopass.fandom.com/wiki/The_Dominator
