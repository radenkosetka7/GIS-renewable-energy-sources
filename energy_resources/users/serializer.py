from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy
from rest_framework import serializers

from .models import UserData


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserData
        fields = (
            'first_name', 'last_name', 'email', 'date_joined', 'is_admin', 'is_staff', 'is_superuser',
            'password', 'password_confirm'
        )

    def validate(self, data):
        err_msg = gettext_lazy("Wrong passwords!")
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError(err_msg)
        else:
            return data

    def create(self, validate_data):
        password = validate_data.pop('password')
        validate_data.pop('password_confirm')
        user = UserData.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_repeated = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserData
        fields = ('old_password', 'password', 'password_repeated')

    def validate(self, data):
        err_msg1 = gettext_lazy("Passwords didn't match!")
        err_msg2 = gettext_lazy("Please enter different new password. This action does not make any changes.")
        if data['password'] != data['password_repeated']:
            raise serializers.ValidationError(err_msg1)
        elif data['password'] == data['old_password']:
            raise serializers.ValidationError(err_msg2)
        else:
            return data

    def validate_old_password(self, value):
        user = self.context['request'].user
        err_msg = gettext_lazy("Wrong old password!")
        if not user.check_password(value):
            raise serializers.ValidationError(err_msg)
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = (
            'first_name', 'last_name', 'email', 'date_joined', 'is_superuser', 'is_admin', 'is_staff',
            'is_active', 'is_superuser'
        )
        read_only_fields = (
            'first_name', 'last_name', 'email', 'date_joined', 'is_superuser', 'is_admin', 'is_staff',
            'is_active', 'is_superuser'
        )
