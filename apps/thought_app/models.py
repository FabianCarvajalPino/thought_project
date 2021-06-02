from django.db import models
from ..logreg_app.models import User
# Create your models here.

class ThoughtManager(models.Manager):
    def thought_validator(self, postData):
        errors = {}
        if len(postData['thought']) < 5:
            errors['thought'] = "El pensamiento debe contener al menos 5 caracteres"
        return errors

class Thought(models.Model):
    owner = models.ForeignKey(User, related_name='thoughts_made', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='thoughts_liked')
    thought = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ThoughtManager()