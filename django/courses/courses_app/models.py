from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData.get('name', '')) < 5:
            errors["title"] = "Name should be at least 5 characters"
        if postData.get('description') and len(postData.get('description')) < 15:
            errors["description"] = "Show description should be at least 15 characters if provided"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    
