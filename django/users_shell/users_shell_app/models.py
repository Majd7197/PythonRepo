from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
                                      
    def __str__(self):
        return f"<User object: name:{self.first_name}{self.last_name} email:{self.email_address} age:{self.age} created at: {self.created_at} updated at:{self.updated_at}>"
