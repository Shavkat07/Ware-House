import base64
import io

from django.core.files import File
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import User


def password_validator(value):
    if len(value) < 8:
        raise ValidationError("This is bad password")
    else:
        return True


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=(password_validator,),
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('password',)


class CheckUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=(password_validator,),
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField()

    def create(self, validated_data):
        password = self.initial_data.get('password', False)

        p = base64.b64decode(self.initial_data.get('avatar', False))
        img = io.BytesIO()
        img.write(p)
        if not password:
            raise ValueError('error')
        validated_data.pop('avatar')
        instance = super().create(validated_data)
        instance.password = make_password(password)
        instance.avatar = File(name=f"avatar_{instance.id}", file=img)
        # instance.is_staff = True
        instance.save()
        return instance

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'avatar', 'email', 'username', 'is_active', 'phone', \
            'user_type'
