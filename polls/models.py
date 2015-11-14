from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    GENDER = (
    	('F', 'Female'),
    	('M', 'Male'),
    )
    gender = models.CharField(max_length = 1, choices = GENDER)
    YEAR_IN_SCHOOL_CHOICES = (
	    ('FR', 'Freshman'),
	    ('SO', 'Sophomore'),
	    ('JR', 'Junior'),
	    ('SR', 'Senior'),
	    ('GR', 'Graduate'),
	)
	year_in_school = models.CharField(max_length = 2, choices = YEAR_IN_SCHOOL_CHOICES)
	major = models.CharField(max_length = 20)

class Course(models.Model):
    pass