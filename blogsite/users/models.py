from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}\'s profile'


# ^(?P<path>.*)$
    # def save(self,*args,**kwargs):
    #     super.save(*args,**kwargs)
    #     #image resize code
