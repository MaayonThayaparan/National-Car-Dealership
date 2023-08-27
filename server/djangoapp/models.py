from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator



# Model for Car Make (ex. Toyota, Honda, etc.)

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Honda')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='Civic')
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    TRUCK = 'Truck'
    VAN = 'Van'
    COUPE = 'Coupe'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (TRUCK, 'Truck'),
        (VAN, 'Van'),
        (COUPE, 'Coupe'),
    ]
    type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )
    dealer_id = models.IntegerField(default=1)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),  # Adjust the minimum year as needed
            MaxValueValidator(2023)   # Adjust the maximum year as needed
        ],
        default=2023
    )

    def __str__(self):
        return f"{self.make.name} {self.name} - {self.year}"


# <HINT> Plain Python class `CarDealer` to hold dealer data. Data comes from Cloundant external service

class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview:
    def __init__(self, id, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year, sentiment):
        # Review id
        self.id = id
        # Review Name
        self.name = name
        # Review Dealership
        self.dealership = dealership
        # Review Review
        self.review = review
        # Review Purchase
        self.purchase = purchase
        # Review Purchase Date
        self.purchase_date = purchase_date
        # Review Car Make
        self.car_make = car_make
        # Review Car Model
        self.car_model = car_model
        # Review Car Year
        self.car_year = car_year
        # Review Sentiment
        self.sentiment = sentiment


