from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app.models import Application
from app.serializers import ApplicationSerializer, UserSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    #permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            print('===========1============')
            if request.POST['api_key']:
                return Response({
                'status': 'error',
                'errors': 'You are not allowed override api key, please leave the field "api_key" empty'
                })
            print('===========2============')

            api_key = Application.generate_key()
            new_data = Application.objects.create(name=request.POST['name'], user=user, api_key=api_key)
            new_data.save()
            serializer = self.get_serializer(new_data)
            return Response({
                'status': 'success',
                'response': serializer.data
            })
        else:
            return Response({
                'status': 'error',
                'errors': 'User is not authenticated'
            })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
