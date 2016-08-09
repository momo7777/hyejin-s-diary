from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class diary_contents(models.Model):
    contents = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=225)
    preparing_person= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)

    def __str__(self):
        return str(self.id)