from django.core.management.base import BaseCommand
import csv
from User_App.models import myUser


class Command(BaseCommand):

    def add_arguments(self, parser) :
        parser.add_argument('No user')

    def handle(self, *args, **options):
        
      with open('user.csv','r') as csv_file:
         csv_reader = csv.reader(csv_file)
         next(csv_reader)
         for line in csv_reader:
            myUser.objects.create(email=line[0],first_name=line[1],last_name=line[2],password=line[3],username=line[4])
    print('done')