from django.db import models

"""
Models: 
	Define the structure of database tables
"""
class Pet(models.Model):
	# Each choice is a tuple where the first value is what is stored in the database, and the second value is used for display in forms and in the django admin.
	SEX_CHOICES = [('M','Male'), ('F','Female')]
	name = models.CharField(max_length=100)
	submitter = models.CharField(max_length=100)
	species = models.CharField(max_length=30)
	breed = models.CharField(max_length=30, blank=True)
	description = models.TextField()
	sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
	submission_date = models.DateTimeField()
	age = models.IntegerField(null=True)
	# This field requires a first argument, which is the name of the model it's related to as a string, so we'll use the string: Vaccine
	vaccinations = models.ManyToManyField(to='Vaccine', blank=True)

# Class to track the vaccine
class Vaccine(models.Model):
	name = models.CharField(max_length=50)

	# String representation
	def __str__(self):
		return self.name