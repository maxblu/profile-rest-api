from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """ test API view """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Returns a list of APIView features
        """

        an_apiview = [
            'Uses HTTP methods as funtions (get,post,patch ,put ,delete)',
            'Is similar to a tradicional djanfo view',
            'Gives the must controls over app logic',
            'Is mapped manualy to Urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create a hello message with a name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})

        else:

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, requests, pk=None):
        """
        Handle updating a object
        """

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Handle a partial update of an object
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Handle delete an object
        """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """
    Test API ViewSet
    """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a helllo message"""

        a_viewset = [
            'Use actions (list,create,retrieve,update ,etc)',
            'Automatically maps to urls using Routers',
            'Provides more funcionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """
        Create a new Hello messge
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Handle getting an object by id
        """

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """
        Handle an update
        """

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """
        Handle partial update
        """
        return Response({"http_method": "PATCH"})

    def destroy(self, requets, pk=None):
        """
        Hnadle delete
        """
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """
        Handle creating and updating
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication token"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    Handles creating reading updating profile feed items
    """
    serializer_class = serializers.ProfileFeedItemSerializer
    # class to manage feed items in the database
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdatingOwnStatus,
        IsAuthenticated  # para verificar si se esta authenticado
    )

    def perform_create(self, serializer):
        """
        Sets the user profile to the logged in user

        (oveeride the behavior of creating and object)

        """

        serializer.save(user_profile=self.request.user)
