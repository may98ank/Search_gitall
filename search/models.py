from django.db import models

# Create your models here.
class Tutorial(models.Model):
    name = models.CharField(max_length = 20)
    path = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.name.lower())
