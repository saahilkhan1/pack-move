from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class SiteUser(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=120,null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    shiftingloc = models.CharField(max_length=200,null=True,blank=True)
    shiftingdate = models.DateField(null=True,blank=True)
    briefitem = models.CharField(max_length=200,null=True,blank=True)
    item = models.CharField(max_length=500,null=True,blank=True)
    requestdate = models.DateField(null=True,blank=True)
    remark = models.CharField(max_length=200,null=True,blank=True)
    status = models.CharField(max_length=20,null=True,blank=True)
    updationdate = models.DateField(null=True,blank=True)
    
    def __str__(self) :
        return self.name
    
class Services(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    image = models.FileField(null=True,blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    contact = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.CharField(max_length=150,null=True,blank=True)
    message = models.CharField(max_length=15,null=True,blank=True)
    mdate = models.DateField(null=True,blank=True)
    isread = models.CharField(max_length=15,null=True,blank=True)
    
    
    def __str__(self) :
        return self.name