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
    course_id=models.CharField(max_length=30)
    course_name=models.CharField(max_length=30)
    course_section=models.CharField(max_length=30)
    COURSE_TYPE=(
        ('Le','Lecture'),
        ('La','Lab'),
        ('Q','Quiz'),   
    )
    course_type=models.CharField(max_length=2,choices=COURSE_TYPE)
    instructor=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    capcity=models.IntegerField()
    registered=models.IntegerField()
    time=models.TimeField()
    # how to add multiple choices?
    days=models.CharField(max_length=30)
    students=models.ManyToManyField(Student)


