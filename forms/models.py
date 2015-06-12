from django.db import models
from django.utils.timezone import now
import datetime
# Create your models here.

class FormsModel(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='static/uploads/')
    date=models.DateField()
    time=models.TimeField()
    price=models.IntegerField()
    address=models.TextField()
    phone=models.IntegerField()
    website=models.URLField()
    neighbourhood=models.TextField()
    description=models.CharField(max_length=200)
    created_at=models.DateTimeField(default=now)