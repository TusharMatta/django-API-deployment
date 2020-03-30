from django.contrib.auth.models import User
from rest_framework import serializers
from userapi.models import Custom_User, UserActivity



class UserActivitySerializer(serializers.ModelSerializer):

	class Meta:
		model = UserActivity
		fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):


	class Meta:
		model = Custom_User
		fields = ['realname', 'continent', 'country', 'activity_periods']

	activity_periods = UserActivitySerializer(read_only=True, many=True)
