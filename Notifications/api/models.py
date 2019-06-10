from mongoengine import *
connect('Cinema', host='mongodb', port=27017)
class Notifications(Document):
    Type =  StringField()
    Title = StringField()
    Content = StringField()
    From = StringField()
    Seat = ListField()
    To = ListField()