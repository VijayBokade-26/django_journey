from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    img = models.FileField(default = "sad.jpg", upload_to="Students_app/Photos")

    
    def __str__(self):
        return self.name
    


    