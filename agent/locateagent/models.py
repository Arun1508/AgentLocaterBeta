from django.db import models

# Create your models here.
class AgentLocations(models.Model):

    id = models.IntegerField(primary_key='True')
    name = models.TextField()
    Address = models.TextField()
    city = models.TextField()
    zipcode = models.IntegerField()
    state = models.TextField()