from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, validators=[MinLengthValidator(9)], blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)  
    image = models.ImageField(upload_to='profile_picture/',blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.username}'s profile"