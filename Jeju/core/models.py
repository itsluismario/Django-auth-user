from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


def PDFFile(instance,filename):
    return 'products/{0}/{1}'.format(instance.name,filename)

class User(AbstractUser):
    email = models.EmailField('email_address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']

class UserProfile(models.Model):
    User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=50, verbose_name="Company name")
    PhoneNumber = models.IntegerField(verbose_name="Phone number", blank=True, null=True)

    def __str__(self):
        return f"user: {self.User.username}"

class Supplier(models.Model):
    Builder = models.ForeignKey(UserProfile, verbose_name="Builder", related_name="BuilderContact", on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=50, verbose_name="Company name")
    Token = models.CharField(max_length=50, blank=True, null=True)
    FirstName = models.CharField(max_length=50, verbose_name="First name")
    LastName = models.CharField(max_length=50, verbose_name="Last name")
    Email = models.EmailField('email_address', unique=True)
    PhoneNumber = models.IntegerField(verbose_name="Phone number", blank=True, null=True)

    def __str__(self):
        return f"user: {self.Supplier.CompanyName}"

class Project(models.Model):
    Builder = models.ForeignKey(UserProfile, verbose_name="Builder", related_name="BuilderContact", on_delete=models.CASCADE)
    ProjectName = models.CharField(max_length=50, verbose_name="Project name")
    Created = models.DateTimeField(verbose_name="Created date",auto_now_add=True)
    Updated = models.DateTimeField(verbose_name="Updated date", auto_now=True)

    def __str__(self):
        return f"user: {self.Project.ProjectName}"

class Quote(models.Model):
    Project = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    Supplier = models.ForeignKey(Supplier, verbose_name="Supplier", related_name="Supplier", on_delete=models.CASCADE)
    QuoteName = models.CharField(max_length=50, verbose_name="Quote name")
    Created = models.DateTimeField(verbose_name="Created date",auto_now_add=True)
    Updated = models.DateTimeField(verbose_name="Updated date", auto_now=True)
    fileUp = models.FileField(upload_to=PDFFile)
    is_upload = models.BooleanField(default=False)

    def __str__(self):
        return f"Quote {self.Quote.QuoteName} for {self.Quote.Project}"

class Material(models.Model):
    Quote = models.ForeignKey(Quote, verbose_name="Project", on_delete=models.CASCADE)
    Supplier = models.ForeignKey(Supplier, verbose_name="Supplier", on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, verbose_name="Name")
    Qty = models.IntegerField(verbose_name="Qty", blank=True, null=True)
    Created = models.DateTimeField(verbose_name="Created date",auto_now_add=True)
    Updated = models.DateTimeField(verbose_name="Updated date", auto_now=True)

    def __str__(self):
        return f"Material: {self.Material.Name}"