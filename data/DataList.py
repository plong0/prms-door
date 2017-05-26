from abc import ABCMeta, abstractmethod
from DataAccess import DataAccess
class DataList(DataAccess):
    """Class to manage a list of database entries"""
    __metaclass__ = ABCMeta

    def __init__(self, config):
        super(DataList, self).__init__(config)

    def list(self, args={}):
        query = self.listSQL(args)
        result = super(DataList, self).query(query)
        entries = []
        # @TODO: handle result as multiple rows
        # foreach result as row
        #   newEntry = self.newEntry()
        #   newEntry.refreshData(row)
        return entries

    @abstractmethod
    def newEntry():
        pass

    @abstractmethod
    def listSQL(self, args={}):
        pass
