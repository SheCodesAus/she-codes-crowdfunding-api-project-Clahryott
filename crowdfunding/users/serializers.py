from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    # ADD password creation / don't worry about password reset

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)  # validated_data means...?

