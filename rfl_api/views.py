from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView): 
    # Test API View 
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None): 
        # Reutrns a list os APIView features
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to a rtaditional Django View', 
            'Gives you the most control over you application logic', 
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request): 
        #  Create a hello message with our name
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message}, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # Handle updating an object
        return Response({'method': 'PUT'})

    def putch(self, request, pk=None): 
        # Handle partial update of an object
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None): 
        # Delete on object
        return Response({'method': 'DELETE'})
         

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    # Test API ViewSet
    def list(self, request):
        # Return a hello message
        a_viewset = [
            'Uses actions(list, create, reuriece, update, partial_update)', 
            'Automatically maps to URLs using Routers', 
            'Provides more functionality with less code', 
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset}, status=status.HTTP_200_OK)

    def create(self, request): 
        # Create a new hello message
        serializer = self.serializer_class(data=request.data) 

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None): 
        # Handle getting an object bu its Id
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None): 
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None): 
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet): 
    # Handle creating and updating profiles

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    
