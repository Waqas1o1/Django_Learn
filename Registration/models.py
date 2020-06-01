from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    reg_Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email