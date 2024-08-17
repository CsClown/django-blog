from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-updated_on']