from django.db import models


# Create your models here.

class Api(models.Model):
    user_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    about = models.CharField(max_length=260)
    added_date=models.DateTimeField(auto_now=True)


