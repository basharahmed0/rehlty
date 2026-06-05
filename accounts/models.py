from django.db import models

# Create your models here.
class payment(models.Model):
    Cardholder_Name = models.CharField(max_length=100)
    Card_Number = models.IntegerField()
    Expiration_Date = models.DateField() 
    cvv = models.IntegerField()
    

    def __str__(self):
        return self.Cardholder_Name

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Account'
class RoomChoices(models.IntegerChoices):
    ONE = 1, '1 Room'
    TWO = 2, '2 Rooms'
    THREE = 3, '3 Rooms'
    FOUR = 4, '4 Rooms'

class PersonChoices(models.IntegerChoices):
    ONE = 1, '1 Person'
    TWO = 2, '2 People'
    THREE = 3, '3 People'
    FOUR = 4, '4 People'
    FIVE = 5, '5 People'
    MORE = 6, '6+ People'

class DataUser(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField()
    checkin = models.DateField()
    checkout = models.DateField()
    number_of_rooms = models.IntegerField()
    number_of_individuals = models.IntegerField()

    def __str__(self):
        return self.fullname
    
    
