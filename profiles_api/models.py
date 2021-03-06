from django.db import models
#necesario para usar el sistema de usuarios de django y modificarlo override
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

from django.contrib.auth.models import BaseUserManager
from django.db.models.base import Model
from django.db.models.fields import CharField
# Create your models here.


class UserProfileManager(BaseUserManager):
    """
        Manager for UserProfiles
    """
    
    def create_user(self,email,name,password= None):
        """ New UserProfile"""

        if not email:
            raise ValueError("User must have email")

        email = self.normalize_email(email)

        user = self.model(email=email,name=name)

        user.set_password(password)

        user.save(using=self._db)

        return user


    
    def create_superuser(self,email,name,password):

        """ Create and save a new superuser"""

        user = self.create_user(email,name,password)

        user.is_superuser= True
        user.is_staff = True
        user.save(using=self._db)
        

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database model for users in the system   """

    email = models.EmailField( max_length=255,unique = True )
    name  = models.CharField(max_length=255  ) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve full name of user"""
        return self.name


    def get_short_name(self):
        """ Retrieve short name of user"""
        return self.name

    def __str__(self):
        """ String representation"""

        return self.email



class ProfileFeedItem(models.Model):
    """
    Profile status update
    """
    
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
     )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)

    def __str__ (self):
        """ return model as string"""

        return self.status_text





