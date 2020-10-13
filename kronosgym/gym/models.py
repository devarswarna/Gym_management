from django.db import models

# Create your models here.
#1
class Enquiry(models.Model):
    name=models.CharField(max_length=60)
    contact=models.CharField(max_length=10)
    email=models.CharField(max_length=60)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)


def __str__(self):
    return self.name
#2
class Equipment(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=10)
    unit=models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    desc=models.CharField(max_length=200)


def __str__(self):
    return self.name

#3
class Plan(models.Model):
    name=models.CharField(max_length=100)
    amount=models.PositiveIntegerField()
    duration=models.CharField(max_length=10)


def __str__(self):
    return self.name

#4
class Member(models.Model):
    name=models.CharField(max_length=50)
    contact=models.PositiveIntegerField()
    email=models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    plan=models.CharField(max_length=40)
    joindate=models.CharField(max_length=50)
    expiredate=models.CharField(max_length=10)
    initalamount=models.CharField(max_length=10)


def __str__(self):
    return self.name
