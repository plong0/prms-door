from flask import Flask
from flask import jsonify

import ConfigParser

from hardware.DoorLock import DoorLock
from hardware.CardReader import CardReader

# initialize Flask app
app = Flask(__name__)

# setup the server
config = ConfigParser.ConfigParser()
config.read('door.ini')

doorLock = DoorLock(config)

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
