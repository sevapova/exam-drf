from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ("username", "password", "role")

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            role=validated_data["role"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "role", "is_active", "created_at")
