from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.CharField(max_length=250)
    year=models.IntegerField()

    image=models.ImageField(upload_to ="movieapp/images",null=True,blank=True)
    def __str__(self):
        return self.name