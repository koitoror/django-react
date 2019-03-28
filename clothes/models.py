from django.db import models

# Create your models here.
class Clothe(models.Model):
    """Clothe model that defines the attributes of the clothe"""
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    clad_type = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_clad_type(self):
        return self.name + ' is a ' + self.clad_type + '.'
    def __repr__(self):
        return self.name + ' is added.'
