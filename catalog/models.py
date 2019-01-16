from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date
import uuid


class Visit(models.Model):
    start = models.DateField(null=True, blank=True)
    stop = models.DateField(null=True, blank=True)

class Architect(models.Model):
    """Model representing an author (arhitect) of the form-factor (plan)"""
    name = models.CharField(max_length=200, help_text='Enter an author (arhitect) name')
    register_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['register_date', 'name']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Contractor(models.Model):
    """Model representing a company who uses the form-factor (plan)"""
    name = models.CharField(max_length=200, help_text='Enter a company name')
    register_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['register_date', 'name']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Consumer(models.Model):
    """Model representing a  of the plan who build for himself"""
    name = models.CharField(max_length=200, help_text='Enter a consumer name')
    register_date = models.DateField(null=True, blank=True)
    visits = models.ForeignKey('Visit', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['register_date', 'name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Plan(models.Model):
    """Model representing a form factor on the development stage. Modifying available here"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular form factor across whole catalog')
    name = models.CharField(max_length=200)
    creation_date = models.DateField(null=True, blank=True)

    approved = models.BooleanField(default=False, help_text='True, if this is moderated approved plan')
    approve_date = models.DateField(null=True, blank=True)
    # for cloning approved plans:
    ancestor_id = models.UUIDField(null=True, blank=True)
    apply_date = models.DateField(null=True, blank=True) # date when plan was added by consumer to his account

    contractor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='contractor')
    consumer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='consumer')

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    architect = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='architect')
    
    #summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    #isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    #genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    class Meta:
        ordering = ['approve_date']
        permissions = (("can_mark_approved", "Can set plan as approved"),("can_create_plan", "Can create plan"),("can_apply_plan", "Can apply plan"),) 
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.name})'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this FormFactor."""
        return reverse('plan-detail', args=[str(self.id)])

