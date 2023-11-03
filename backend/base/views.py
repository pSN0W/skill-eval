from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def get_routes(request):
    """View to display all the endpoints"""
    routes = {
        "none": "no routes created yet"
    }
    return Response(routes)