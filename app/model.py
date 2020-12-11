from application import db

class Device(db.Model):
    deviceid = db.Column('deviceid', db.Integer, primary_key=True)
    devicetype = db.Column('devicetype', db.String(50))
    name = db.Column('name', db.String(50))
    event = db.Column('event', db.String(500))# for example: '[calling, leaving]'

    def __init__(self, id, devicetype, name, event):
        self.deviceid = id
        self.devicetype = devicetype
        self.name = name
        self.event = str(event)

    def __rep__(self):
        return '<Device {0}, type: {1}>'.format(self.deviceid, self.devicetype)
