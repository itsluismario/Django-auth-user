from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import AbstractUser

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
    Builder = models.ManyToManyField(UserProfile)
    CompanyName = models.CharField(max_length=50, verbose_name="Company name")
    Token = models.CharField(max_length=50, blank=True, null=True)
    FirstName = models.CharField(max_length=50, verbose_name="First name")
    LastName = models.CharField(max_length=50, verbose_name="Last name")
    Email = models.EmailField('email_address', unique=True)
    PhoneNumber = models.IntegerField(verbose_name="Phone number", blank=True, null=True)

    def __str__(self):
        return f"user: {self.CompanyName}"

class Project(models.Model):
    Builder = models.ForeignKey(UserProfile, verbose_name="Builder", on_delete=models.CASCADE)
    ProjectName = models.CharField(max_length=50, verbose_name="Project name")
    Created = models.DateTimeField(verbose_name="Created date",auto_now_add=True)
    Updated = models.DateTimeField(verbose_name="Updated date", auto_now=True)

    def __str__(self):
        return f"Project: {self.ProjectName}"

class ItemCategory(models.Model):
    Category = models.CharField(max_length=50, verbose_name="Category")
    def __str__(self):
        return f"Category: {self.Category}"

class ItemView(models.Model):
    View = models.CharField(max_length=50, verbose_name="View")
    def __str__(self):
        return f"View: {self.View}"

class ItemUnit(models.Model):
    Unit = models.CharField(max_length=50, verbose_name="Units")
    def __str__(self):
        return f"Units: {self.Unit}"
    
class Item(models.Model):
    Name = models.CharField(max_length=50, verbose_name="Name")
    ItemCategory = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    ItemView = models.ForeignKey(ItemView, on_delete=models.CASCADE)
    ItemUnit = models.ForeignKey(ItemUnit, on_delete=models.CASCADE)
    Created = models.DateTimeField(verbose_name="Created date",auto_now_add=True)
    Updated = models.DateTimeField(verbose_name="Updated date", auto_now=True)

    def __str__(self):
        return f"Item: {self.Name}"
    
class QuoteHeader(models.Model):
    Supplier = models.ManyToManyField(Supplier)
    Project = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    QuoteName = models.CharField(max_length=50, verbose_name="Quote name")
    FileUp = models.FileField(upload_to='PDFFile',blank=True, null=True)
    IsUpload = models.BooleanField(default=False)
    Total = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    Quantity = models.IntegerField(blank=True, null=True)
    IsActive = models.BooleanField(default=True)
    Created = models.DateTimeField(verbose_name="Created date",auto_now_add=True)
    Updated = models.DateTimeField(verbose_name="Updated date", auto_now=True)

    def __str__(self):
        return f"Quote header of {self.QuoteName} for {self.Project}"

def quote_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/project_<nameproject>/<filename>
    return 'user_{0}/project_{1}/{2}'.format(instance.user.id,instance.user.project, filename)

class QuoteFile(models.Model):
    File = models.FileField(upload_to = quote_directory_path)

class QuoteBody(models.Model):
    QuoteHeader = models.ForeignKey(QuoteHeader, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE,blank=True, null=True)
    Subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    QuantityByItems = models.IntegerField()
    QuoteFile = models.ForeignKey(QuoteFile, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"Quote body of {self.Item} for {self.QuoteHeader.QuoteName}"


    
