from django.db import models
from login.models import EmployeeAccount
class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    startDate = models.DateField(default=None, null=True, blank=True)
    endDate = models.DateField(default=None, null=True, blank=True)
    description = models.TextField()
    current = models.BooleanField(default=False)

    
class Education(models.Model):
    establishment = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateField(default=None, null=True, blank=True)
    current = models.BooleanField(default=False)

    
class Skill(models.Model):
    skill = models.CharField(max_length=255)

    
class Language(models.Model):
    language = models.CharField(max_length=255)
    level = models.CharField(max_length=255)


class Interests(models.Model):
    interest = models.CharField(max_length=255)
    
class Certification(models.Model):
    certificate = models.CharField(max_length=255)
    platforme = models.CharField(max_length=255)
    dateD = models.DateField(default=None, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/')


class Community(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    startDate = models.DateField(default=None, null=True, blank=True)
    endDate = models.DateField(default=None, null=True, blank=True)
    description = models.TextField()

    
class Profile(models.Model):
    employee_account = models.OneToOneField(
        EmployeeAccount,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    avatar = models.ImageField(default="avatar.svg", null = True )
    profileTitle = models.CharField(max_length=255)
    profileDescription = models.TextField()
    phone = models.CharField(null = True, max_length=100) 
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=4)
    birthDate = models.DateField(default=None, null=True, blank=True)
    gender = models.CharField(max_length=6, choices= [('M','male'), ('F', 'female')], null = True )
    linkedin = models.URLField(max_length=200, null = True) 
    certifications = models.ManyToManyField(Certification, blank=True)
    communities = models.ManyToManyField(Community, blank=True)
    interests = models.ManyToManyField(Interests, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    educations = models.ManyToManyField(Education, blank=True)
    experiences = models.ManyToManyField(Experience, blank=True)
        

