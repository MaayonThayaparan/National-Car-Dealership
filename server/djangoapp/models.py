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


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
