from mongoengine import *
connect('Cinema', host='mongodb', port=27017)

class Bookings(Document):
    UserID = GenericReferenceField( required=True )
    Cinema = StringField()
    Movie = StringField()
    Schedule = StringField()
    Seat = ListField()
    TotalAmount = FloatField()

class Tickets(Document):
    Cinema = StringField()
    Movie = StringField()
    Schedule = StringField()
    Seat = ListField()
    Status = StringField(default = "Spending")
    BookingID = GenericReferenceField( required=True )

class Users(Document):
    username = StringField()
    password = StringField()
    fullname = StringField()
    Email = StringField(require=True)