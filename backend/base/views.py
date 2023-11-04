from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializerWithToken
from .models import User
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Creating our custom serializer for Token"""
    def validate(self,attrs):
        """Overriding the validate function
        This function returns the data that is returned when user is authenticated
        """
        data = super().validate(attrs)
        
        # Serializing the current User
        serializer = UserSerializerWithToken(self.user).data
        
        # Populating the data dictionary with data returned from serializer
        for k,v in serializer.items():
            data[k] = v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    """Creating our own custom view to use our serializer"""
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def get_routes(request):
    """View to display all the endpoints"""
    routes = {
        "login" : "To authenticate a user",
        "users/create" : "Create a new user",
    }
    return Response(routes)

@api_view(['POST'])
def create_user(request):
    """APIView to create User"""
    data = request.data
    
    # Try creating the user with username and password
    try:
        user = User.objects.create(
            username = data['username'],
            password = make_password(data['password'])
        )
    except:
        message = {'detail':"User with this username already exists"}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    
    # If first name and last name provided then update the user
    user.email = data.get('email','')
    user.name = data.get('name','')
    user.organisation = data.get('organisation','')
    user.save()
    
    # Once the user has been created return the information of user with token
    serializer = UserSerializerWithToken(user)
    return Response(serializer.data)