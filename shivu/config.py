class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5886080930"
    sudo_users = "5886080930", "6312685867", "5268691896"
    GROUP_ID = -1002137208192
    TOKEN = "6707490163:AAHZzqjm3rbEZsObRiNaT7DMtw_i5WPo_0o"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "https://t.me/kill_your_HW_Group"
    UPDATE_CHAT = "https://t.me/kill_your_HW_Channel"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002137208192"
    api_id = 25504446
    api_hash = "47db27cde56c3e4690e244e6de10f919"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
