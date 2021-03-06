from rest_framework import generics
import factory  
import factory.django
from userapi.models import Custom_User, UserActivity
from userapi.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

class UserList(generics.ListCreateAPIView):
	queryset = Custom_User.objects.all()
	serializer_class = UserSerializer



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Custom_User.objects.all()
	serializer_class = UserSerializer



def index(request):
	return HttpResponse('<h1>Welcome to my API Home Page</h1')


@csrf_exempt
@api_view(['GET'])
def user_view(request):

	if(request.method == 'GET'):
		users = Custom_User.objects.all()
		serializer1 = UserSerializer(users, many=True)

		status=True
		
		final_dict = {'ok':status, 'members':serializer1.data}
		return Response(final_dict)





class UserFactory(factory.django.DjangoModelFactory):  
	class Meta:
		model = 'userapi.Custom_User'
		

class UserActivityFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = 'userapi.UserActivity'
