from django.db import models

# Create your models here.
class Hospital (models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200, default = 'address')
    city = models.CharField(max_length = 100, default = 'city')


    #Hospital images {install pillow to work(python -m pip install Pillow)}
    # image_one = models.ImageField(upload_to='images/')
    # image_two = models.ImageField(upload_to='images/')
    # image_three = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.id} {self.name}'
