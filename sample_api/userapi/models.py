from django.db import models



class Custom_User(models.Model):

	realname = models.CharField(max_length=50)
	continent = models.CharField(max_length=15, blank=True)
	country = models.CharField(max_length=25, blank=True)


	def __str__(self):
		return (str(self.pk) + '-' + self.realname)


class UserActivity(models.Model):

	custom_users_id = models.ForeignKey('Custom_User', related_name='activity_periods', on_delete=models.CASCADE, default='')
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	end_time = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return str(self.id)