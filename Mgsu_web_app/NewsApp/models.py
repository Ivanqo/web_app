from django.db import models
from django.utils import timezone
import random

# Create your models here.

def generate_random_colour():
    return random.randint(0, 3)

class New(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    colour = models.IntegerField(default=generate_random_colour)
    image = models.ImageField(upload_to='img\\', null=True, blank=True)

    def __str__(self):
        return self.title
