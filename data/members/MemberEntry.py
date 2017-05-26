from data.DataEntry import DataEntry
class MemberEntry(DataEntry):
    """Class to manage a Member entry"""

    def __init__(self, config, data=None):
        super(MemberEntry, self).__init__(config, data)

    def loadSQL(self, args):
        # @TODO: build the select member query
        return "SELECT * FROM members WHERE id=%s LIMIT 1" % (args['id'])

    def insertSQL(self, data):
        # @TODO: return the SQL statement for inserting member data
        return "INSERT INTO members(name), VALUES('%s')" % (data.name)

    def updateSQL(self, data):
        super(MemberEntry, self).updateSQL(data)
        # @TODO: return the SQL statement for updating member data
        return "UPDATE members SET name='%s' WHERE id=%s" % (data.name, data['id'])
