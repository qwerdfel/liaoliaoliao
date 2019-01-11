from django.db import models

# Create your models here.
class User(models.Model):
    phonenum = models.IntegerField(max_length=20)
    nickname = models.CharField(max_length=24)
    sex = models.IntegerField(default=1)
    birth_year = models.DateField(max_length=10)
    birth_month = models.DateField(max_length=10)
    birth_day = models.DateField(max_length=10)
    avater = models.ImageField(max_length=255)
    location = models.CharField(max_length=128)

    class Meta:
        db_table = "user"









