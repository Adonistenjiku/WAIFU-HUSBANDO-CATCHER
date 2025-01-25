class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5886080930"
    sudo_users = "5886080930", "7972319522","5268691896"
    GROUP_ID = -1002137208192
    TOKEN = "6978354290:AAF-j6QEGYRPd-uwy3oE4mF2xjPuUIdrkPQ"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://unitedcamps.in/Images/file_11559.jpg", "https://unitedcamps.in/Images/file_11413.jpg"]
    SUPPORT_CHAT = "https://t.me/kill_your_HW_Group"
    UPDATE_CHAT = "https://t.me/kill_your_HW_Channel"
    BOT_USERNAME = "@Kill_your_Husbando_bot"
    CHARA_CHANNEL_ID = "-1002137208192"
    api_id = 25504446
    api_hash = "47db27cde56c3e4690e244e6de10f919"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
