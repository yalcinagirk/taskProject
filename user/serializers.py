from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_staff=True
        )
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']