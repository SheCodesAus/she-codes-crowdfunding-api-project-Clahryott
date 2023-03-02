from rest_framework import serializers
from .models import CustomUser
import random
import string

# ADD password creation / don't worry about password reset
    

# use of Model Serializer to save time on setting password
def random_username(): ######### ?????
    letters = string.ascii_lowercase
    result_username = ''.join(random.choice(letters) for i in range(7))
    return result_username

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: #this means you don't need to also then put in models.py --- why I don't know, but it does ******
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']
        read_only_fields = ['id'] 
        extra_kwargs = {'password' : {'write_only' : True}}
    
    def create(self, validated_data): # # # # # # ???
        user = CustomUser (
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class CustomUserDetail(CustomUserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password')
        read_only_fields = ['id']


# NEED TO ADD CHANGE PASSWORD FUNCTION - check users/models.py

#class ChangePassword(serializers.Serializer):

    #model = CustomUser
    #what to add - search GITs 