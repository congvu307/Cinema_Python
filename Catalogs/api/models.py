from mongoengine import *
connect('Cinema', host='mongodb', port=27017)

class Cities(Document):
    name = StringField()

class CinemaRooms(Document):
    CityID = GenericReferenceField( required=True )
    Location = StringField()
    Name = StringField()
    Capacity = FloatField()
    Type = StringField()
    Flot = StringField()

class Schedules(Document):
    Time = StringField()
    CinemaRoomID = GenericReferenceField( required = True )
    seatsEmpty = ListField()
    seatsOccupied = ListField()
    price = FloatField()
    MovieID = StringField()
    
# Create your models here.
