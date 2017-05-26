from abc import ABCMeta
class DataAccess:
    """Database access base class - handles low-leve database routines"""
    __metaclass__ = ABCMeta

    # shared db connection
    db = None

    def __init__(self, config):
        self.config = config
        self.db = None

    def _assertConnection(self):
        if (self.db is None):
            self.db = self.connect()
        return self.db

    def connect(self):
        if (DataAccess.db):
            return DataAccess.db;
        # @TODO: if no existing connection, create one
        DataAccess.db = {}
        print "Created new DataAccess.db!"
        self.db = DataAccess.db;
        return self.db

    def disconnect(self):
        if (DataAccess.db):
            # @TODO: disconnect from database server
            DataAccess.db = None
        self.db = DataAccess.db

    def query(self, query):
        self._assertConnection()
        print "Running Query: %s" % query
        # @TODO: execute the query
        # @TODO: return the result
        return None
