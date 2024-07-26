from django.db import models
import re
from datetime import datetime


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not (postData.get('first_name') and postData.get('last_name') and postData.get('email') and postData.get('password') and postData.get('confirm_password')):
            errors["fields"] = "All fields must be present"
        
        if len(postData.get('first_name', '')) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if len(postData.get('last_name', '')) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
            
        email = postData['email']
        if User.objects.filter(email=email).exists():
            errors['unique', ''] = "This email address is already used"
            
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):             
            errors['email'] = "Invalid email address!"
        if len(postData.get('password', '')) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData.get('confirm_password', '') != postData.get('password', '') :
            errors["confirm_password"] = "Both passwords must be identical!"
        return errors
    
class PieManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not (postData.get('name')):
            errors["name"] = "name must be present"
        if not (postData.get('filling')):
            errors["filling"] = "Please Include the Filling"
        if not (postData.get('crust')):
            errors["crust"] = "Please Include the crust"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class Pie(models.Model):
    name = models.CharField(max_length = 255)
    filling = models.CharField(max_length = 255)
    crust= models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="pies", on_delete=models.CASCADE)
    objects = PieManager()
        
        

    
