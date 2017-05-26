from abc import ABCMeta, abstractmethod
from DataAccess import DataAccess
class DataEntry(DataAccess):
    """Class to manage a single database entry"""
    __metaclass__ = ABCMeta

    def __init__(self, config, data=None):
        super(DataEntry, self).__init__(config)
        self.data = {}
        if (data):
            self.refreshData(data)

    def load(self, args):
        query = self.loadSQL(args)
        result = super(DataEntry, self).query(query)
        # @TODO: handle result as a single row
        #return self.refreshData(result)
        return result

    def refreshData(self, data):
        # basic property copying, anything more advanced should override
        for prop, value in data.__dict__.iteritems():
            self.data[prop] = value
        return self.data

    def save(self, data):
        if (data.id is None):
            query = self.insertSQL(data)
        else:
            query = self.updateSQL(data)
        if (query):
            saved = super(DataEntry, self).query(query)

    @abstractmethod
    def loadSQL(self, args):
        pass

    @abstractmethod
    def insertSQL(self, data):
        pass

    @abstractmethod
    def updateSQL(self, data):
        if (data.id is None):
            raise ValueError('Cannot update DataEntry: Missing id')
        pass
