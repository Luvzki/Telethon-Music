import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6389827842:AAEW6lYfCsDdeukJYXZaMWSTayy73ibemuM)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOH8Bux4l7fBeAhq8wyHQlJ0mO1R8EM-qodwfR1Ikiqpl4m-p77eoqAskPQfm5vjqfhyF9U1_36yj5C8izF3hX_JyB4_VmZ6GSbRIg5mM64A6QcyGt8mjgEH485Auzi6Belg0BnjLAA_9T8CST7iFRDxDVGHqVttZ1lMHY_mQtq5r1sHdupvRJvzYP2FFnkLePVVYpUHkvqqkx7PoSm-4JFmUnQVgNRc5OVe62X76ru5_8ZuzvD9FKn0AbLBOQy5uJj9eTzQs-s3cVsx1ae6sh-8BmThgXm9dItm2zKbry4Al7AON3Eqg67q3wck4YojJpP9bYNrKqJX6COeFPbfYjaI9ctY=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
