from django.db import models

# Create your models here.

class Incident(models.Model):
    STATUS_CHOICES = [('ACTIVE', 'Active'), ('CLOSED', 'Closed')]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    latitude =models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    def __str__(self):
        return self.title
