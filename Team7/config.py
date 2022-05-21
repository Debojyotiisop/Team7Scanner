import json
import os


def get_user_list(config, key):
    with open("{}/EnmuBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    OWNERID = [2093473332,5146000168]
    INSPECTORS = [1537076718,5001573230,2070119160,5069705982,5147265129,1242979521,2131857711,5213143273,837914403,1608911105,5278295844,1883976677,998589443,1789859817,5292346355]
    ENFORCER = [1866990348,1371324664,1098395252]
    Sibyl_Approved_Logs = (-1001525807961)
    GBAN_MSG_LOGS = (-1001525132581)
    BOT_TOKEN = "5394211831:AAEQEU_doh1wqoxT5i1cq9N3tfsGTJHpiSY"
    MONGO_DB_URL = "mongodb+srv://scan:scan123@scanner.xxtiq.mongodb.net/?retryWrites=true&w=majority"
    Sibyl_logs = (-1001525807961)
    STRING_SESSION = "1BVtsOK4Bu7_48BNrPO3Zaee9GSk8nQI0Ii9X6q0aEzbZF1XSv9AA5iquVWtvBJXLrNgFjuVnR768s-UWuoOyye927ii9ir6FB9nO-qJqa0JuhZipgSb0EMfrcLDE6BwpGb4NWT__5GynoHde0tiBH5NzwxUE5ESPb7c2MKvQzDExTZU9vrGGUBEpSSK9Ri-b_DE5244rgRqm0flCl4x4T0EnNSsZHkIO0Px0hEcS08W5Yhacp3nViu5KCMrqi_72a0jY7sdE_Mykd9S24IR1DS6GKgtLvOVPrzhYN8MXWtU7vr99KIdT2mWGiKR_Z5o-bXhFVAEmTL2QmOXTMNlFQhBhwLD4udc="
