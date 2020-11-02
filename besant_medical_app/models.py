from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class RegisterData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    mobile = models.BigIntegerField()
    customer = models.CharField(max_length=20)
    docfile = models.ImageField(upload_to='images/')






class Medstoringsupplier(models.Model):
    tabletname = models.CharField(max_length=100)
    brandname = models.CharField(max_length=100)
    components = models.CharField(max_length=500)
    price = models.CharField(max_length=100)


class Medmedicalshop(models.Model):
    tabletname = models.CharField(max_length=100)
    brandname = models.CharField(max_length=100)
    components = models.CharField(max_length=500)
    price = models.CharField(max_length=100)


class Supquantmanagmnt(models.Model):
    brandname = models.CharField(max_length=500)
    tablename = models.CharField(max_length=500)
    components = models.CharField(max_length=500)
    quantity = models.IntegerField()
    soldtablets = models.IntegerField()
    availablestock = models.IntegerField()

class Medicalquantmgnt(models.Model):
    brandname = models.CharField(max_length=500)
    tablename = models.CharField(max_length=500)
    components = models.CharField(max_length=500)
    quantity = models.IntegerField()
    soldtablets = models.IntegerField()
    availablestock = models.IntegerField()


