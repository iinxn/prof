from django.db import models

class Personal(models.Model):
  last_name = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  sur_name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  organization = models.CharField(max_length=50)
  mark = models.CharField(max_length=50)
  date = models.DateField()
  serias = models.IntegerField()
  number = models.IntegerField()
  image = models.ImageField(upload_to='images/')
  def __str__(self):
      return self.first_name
    
class Group(models.Model):
  last_name = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  sur_name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  organization = models.CharField(max_length=50)
  mark = models.CharField(max_length=50)
  date = models.DateField()
  serias = models.IntegerField()
  number = models.IntegerField()
  image = models.ImageField(upload_to='images/')
  def __str__(self):
    return self.first_name
