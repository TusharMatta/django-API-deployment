from django.core.management.base import BaseCommand
from faker import Faker
import random

# import UserFactory here
from userapi.views import UserFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
        	default=1,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
    	f = Faker()
    	continent_list = ['Asia', 'Europe', 'Australia', 'North America', 'South America', 'Antarctica', 'Africa']
    	for _ in range(options['users']):
    		UserFactory.create(realname=f.name(), continent=random.choice(continent_list), country=f.country())