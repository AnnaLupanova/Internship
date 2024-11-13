from rest_framework import viewsets
from .models import User, Order
from .serializers import UserSerializer, OrderSerializer
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response({
                'error': 'Integrity Error',
                'message': str(e),
            }, status=400)
        except ValidationError as e:
            return Response({
                'error': 'Validation Error',
                'message': str(e),
            }, status=400)
        except Exception as e:
            return Response({
                'error': 'Unexpected Error',
                'message': str(e),
            }, status=500)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user')).first()
        if not user:
            raise NotFound("User not found")
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response({
                'error': 'Integrity Error',
                'message': str(e),
            }, status=400)
        except ValidationError as e:
            return Response({
                'error': 'Validation Error',
                'message': str(e),
            }, status=400)
        except Exception as e:
            return Response({
                'error': 'Unexpected Error',
                'message': str(e),
            }, status=500)
