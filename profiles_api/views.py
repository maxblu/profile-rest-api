from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """ test API view """

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
    

