from django.db import models
class Passwords(models.Model):
    title = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add=True)

# Create your models here.
