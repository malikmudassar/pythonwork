from django.db import models

class Uploader(models.Model):
    file=models.FileField(upload_to="uploads")


class dataSet (models.Model):
    ds_name=models.CharField(max_length=50)
    pair=models.CharField(max_length=50)
    time=models.CharField(max_length=60)
    _id=models.IntegerField()
    price=models.FloatField()
    volume=models.FloatField()
    side=models.CharField(max_length=50)