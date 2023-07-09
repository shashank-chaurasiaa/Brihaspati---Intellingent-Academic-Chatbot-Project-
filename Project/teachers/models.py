from django.db import models

# Create your models here.

class Teacher(models.Model):
    text = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.text
       



    


