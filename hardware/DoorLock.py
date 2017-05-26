from utils import enum

class DoorLock:
    """Class to manage the Door Lock"""
    STATUS = enum(UNLOCKED=0, LOCKED=1)

    def __init__(self, config):
        self.config = config;
        self.status = DoorLock.STATUS.UNLOCKED

    def lock(self):
        # @TODO: copy code from door.py
        self.status = DoorLock.STATUS.LOCKED

    def unlock(self):
        # @TODO: copy code from door.py
        self.status = DoorLock.STATUS.UNLOCKED

    def getStatus(self, asString=False):
        if (asString):
            return DoorLock.STATUS.reverse_mapping[self.status]
        return self.status
