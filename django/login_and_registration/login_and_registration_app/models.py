from django.db import models
import re
from datetime import datetime


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData.get('first_name', '')) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if len(postData.get('last_name', '')) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
            
        birthday = datetime.strptime(postData.get('birthday', ''), '%Y-%m-%d')
        if birthday:
            if birthday > datetime.now():
                errors["birthday"] = "Birthday Should be in the past"
        else:
            errors["birthday"] = "Please Provide Your Birthday"
            
        email = postData['email']
        if User.objects.filter(email=email).exists():
            errors['unique', ''] = "This email address is already used"
            
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData.get('password', '')) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData.get('confirm_password', '') != postData.get('password', '') :
            errors["confirm_password"] = "Both passwords must be identical!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    
