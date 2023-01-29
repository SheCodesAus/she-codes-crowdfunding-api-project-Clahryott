from rest_framework import serializers
from .models import CustomUser

#class CustomUserSerializer(serializers.Serializer): ----- NOT needed as changed to ModelSerializer instead.
    #id = serializers.ReadOnlyField()
    #username = serializers.CharField(max_length=150)
    #email = serializers.EmailField()

    #def create(self, validated_data):
        #return CustomUser.objects.create(**validated_data)  

# ADD password creation / don't worry about password reset
    

# use of Model Serializer to save time on setting password
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: #this means you don't need to also then put in models.py --- why I don't know, but it does ******
        model = CustomUser
        fields = ['email', 'username', 'password']
        read_only_fields = ['id'] 
        extra_kwargs = {'password' : {'write_only' : True}}
    
    def create(self, validated_data):
        user = CustomUser (
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user