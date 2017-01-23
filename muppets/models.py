import json
from django.db import models

# Create your models here.

class Muppet(models.Model):

    name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)

    def json_output(self):
        return {
            'name': self.name,
            'id': self.id,
            'occupation': self.occupation
        }