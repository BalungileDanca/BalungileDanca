from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class userManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
     
    def create_superuser(self,username, email, password):
          user = self.create_user(username,email, password)
          user.is_staff = True
          user.is_superuser = True
          user.save(using= self._db)
          return user
class user(AbstractUser):
      email = models.EmailField(unique= True, max_length=255)
      username = models.CharField(unique= True, max_length=10)

      object = userManager()
      USERNAME_FIELD = 'username'
      REQUIRED_FIELDS = ['email']
    

