from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer ):
    """
    Serializes a name field for testing our APIView
    """
    
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer ):
    """
    Serializes a user profile object
    """
    
    class Meta:
        # modelo que se quiere serializar seguidp de los capos del mismo que se quieren hacer publicos a la api
        model = models.UserProfile
        fields = ('id','name','email','password')
        
        #estos valores son para indicar cosideraciones sobre algunos de los campos para no devolverlos siempre
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self,validated_data):
        """ Create a return a new user"""

        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name= validated_data['name'],
            password= validated_data['password']
        )

        return user


    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)