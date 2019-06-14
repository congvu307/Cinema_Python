from mongoengine import *
connect('Cinema', host='localhost', port=27017)

class Bookings(Document):
    UserID = GenericReferenceField( required=True )
    Cinema = StringField(max_length=40,required=True)
    Movie = StringField(max_length=40,required=True)
    Schedule = StringField(max_length=40,required=True)
    Seat = ListField(required=True)
    TotalAmount = FloatField()

class Tickets(Document):
    Cinema = StringField()
    Movie = StringField()
    Schedule = StringField()
    Seat = ListField()
    Status = StringField(default = "Spending")
    BookingID = GenericReferenceField( required=True )

class Users(Document):
    username = StringField(max_length=10)
    password = StringField(max_length=10)
    fullname = StringField(require=True)
    Email = StringField(require=True)