from django.core.management.base import BaseCommand
from typing import Any

# create custom manage.py command --> python manage.py hello_world
class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print('Hello World')