from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "8479389"))
API_HASH = getenv("API_HASH", "f75e6f068c8bb9b8c884484ea2c6177b")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5445522355:AAGf7MnB-ajkbe5aQcdBq_vstB4M-5lMkYE")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001554007729"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Ziddiboy:vijayrao1703@cluster0.4wbux.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1962673406").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Lobe_JU")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/Oye_golgappu")

STRING_SESSION = getenv("STRING_SESSION", "BQA7T_7W94chxAAdOfrSpGflupufU3OGVSvKG_4auY-5ZtaFPc1EzLvO6WJ6M8BbMz-ygu0wbE3BHQKOSfW6r9Pl46oof7WQilUlQhx982bPbLH-xXxJUOPsh8arefBChlz48ZB_7Bj4ikqxnAr5RomW0ijwgeNe26lMvbNkCZIXhncQS_EtlfV2Rn4q7pGrS9-FXi1AC1L7O1p4LZ31owYnpfFJNE7hr5UNWAH5LYmFc2EeG1tiz8eP2t44U2ztMA82S00eYF2zlOeHqbuov-q2uVWdvBW5V96PQHH1hE1mXzCJc2Q-xIOrOTpGrCwQbHm8tv-oaiNvK__miFB8jjByAAAAAHTel-MA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1962673406").split()))
