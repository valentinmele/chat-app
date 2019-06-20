# Logs chats messages
from datetime import datetime

class Logger:
    """Logs messages."""

    def __init__(self, log_path):
        self.log = open(log_path, "a+")

    def message(self, room, author, message):
        entry = "[{}] {} - {}: {}".format(str(datetime.now()), room, author, message)
        print(entry)
        self.log.write(entry + "\n")

    def register(self, username):
        entry = "[{}] {} has just registered.".format(str(datetime.now()), username)
        print(entry)
        self.log.write(entry + "\n")

    def login(self, username):
        entry = "[{}] {} is now logged in.".format(str(datetime.now()), username)
        print(entry)
        self.log.write(entry + "\n")

    def logout(self, username):
        entry = "[{}] {} has just disconnected.".format(str(datetime.now()), username)
        print(entry)
        self.log.write(entry + "\n")

    def __del__(self):
        self.log.close()