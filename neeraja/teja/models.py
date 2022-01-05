from django.db import models
class next(models.Model):
    name=models.CharField(max_length=20)

    address=models.TextField()
    phonenumber=models.BigIntegerField(null=True)


    def __str__(self):
        return self.name

# Create your models here.
