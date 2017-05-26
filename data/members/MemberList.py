from data.DataList import DataList
from MemberEntry import MemberEntry
class MemberList(DataList):
    """Class to manage a list of Members"""

    def __init__(self, config):
        super(MemberList, self).__init__(config)

    def newEntry(self):
        return MemberEntry(self.config)

    def listSQL(self, args):
        # @TODO: build the list members query
        return "SELECT * from members"

    def synchronizeWA(self, args=None):
        pass
