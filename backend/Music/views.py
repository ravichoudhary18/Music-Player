from rest_framework.views import APIView
from rest_framework.response import Response 

class TestAPI(APIView):

    def get(request):
        return Response({"massage": "Server is running", "status": 200})