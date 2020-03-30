from django.core.management.base import BaseCommand
from faker import Faker
import random
from userapi.models import Custom_User

# import UserFactory here
from userapi.views import UserActivityFactory



class Command(BaseCommand):
	help = 'Seeds the database.'

	def add_arguments(self, parser):
		parser.add_argument('--users',
			default=1,
			type=int,
			help='The number of fake users to create.')

	def handle(self, *args, **options):
		custom_user_data = Custom_User.objects.all()
		
		f = Faker()

		s_time = f.time()
		# end_time = s_time
		month = f.month()
		day = f.day_of_month()
		year = f.year()

		date = '{}-{}-{} {}'.format(year, month, day, s_time[:-3])

		for i in custom_user_data:
			UserActivityFactory.create(custom_users_id=i,start_time=date, end_time=date)