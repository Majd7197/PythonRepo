from django.db import models
from datetime import date

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData.get('title', '')) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if postData.get('description') and len(postData.get('description')) < 10:
            errors["description"] = "Show description should be at least 10 characters if provided"
        if len(postData.get('network', '')) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if postData.get('release_date'):
            release_date = postData.get('release_date')
            if release_date >= str(date.today()):
                errors["release_date"] = "Release date should be in the past"
        else:
            errors["release_date"] = "Release date is required"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()
