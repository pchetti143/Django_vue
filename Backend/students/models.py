from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=500)
    course=models.CharField(max_length=500)
    rating=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['name']