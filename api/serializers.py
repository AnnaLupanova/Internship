from rest_framework import serializers
from .models import User, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'title', 'description', 'user']

    def validate(self, data):
        if not data.get('title') or len(data['title']) < 3:
            raise serializers.ValidationError("The title of the order must be at least 3 characters long.")
        elif Order.objects.filter(title=data.get('title')).exists():
            raise serializers.ValidationError("Order with this title already exists.")
        return data
