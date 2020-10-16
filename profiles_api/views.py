from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers



class HelloApiView(APIView):
    """ test API view """

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """
        Returns a list of APIView features
        """
        
        an_apiview = [
            'Uses HTTP methods as funtions (get,post,patch ,put ,delete)',
            'Is similar to a tradicional djanfo view',
            'Gives the must controls over app logic',
            'Is mapped manualy to Urls'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
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


    def put(self, requests,pk=None):
        """
        Handle updating a object
        """
        

        return Response({'method':'PUT'})


    def patch(self, request,pk=None):
        """
        Handle a partial update of an object
        """
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """
        Handle delete an object
        """
        return Response({'method':'DELETE'})

        