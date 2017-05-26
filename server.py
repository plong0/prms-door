from flask import Flask
from flask import jsonify

import ConfigParser

from hardware import DoorLock, CardReader
from data.members.MemberList import MemberList
from data.members.MemberEntry import MemberEntry

# initialize Flask app
app = Flask(__name__)

# setup the server
config = ConfigParser.ConfigParser()
config.read('door.ini')

doorLock = DoorLock.DoorLock(config)
memberList = MemberList(config)

@app.route('/')
def welcome():
    return jsonify({"message": "Twinkle, twinkle, little bat\n\
How I wonder what you're at\n\
Up above the world you fly\n\
Like a teatray in the sky"})

@app.route('/door')
@app.route('/door/status')
def door_status():
    return jsonify({
        "status": doorLock.getStatus(),
        "message": "The door is %s" % (doorLock.getStatus(True))
        })

@app.route('/door/lock')
def door_lock():
    doorLock.lock()
    return door_status()

@app.route('/door/unlock')
def door_unlock():
    doorLock.unlock()
    return door_status()

@app.route('/members')
@app.route('/members/list')
def list_members():
    members = memberList.list()
    return jsonify({
        "members": members,
        "message": "There are %d members in the system" % (len(members))
        })

@app.route('/members/refresh')
def refresh_members():
    memberList.synchronizeWA()
    return list_members()

@app.route('/members/<id>')
def get_member(id):
    member = MemberEntry(config)
    member.load( {"id":id} )
    return jsonify({
        "member": member.data
        })
