from django.core.management.base import BaseCommand
from ...models import *
from datetime import date

class Command(BaseCommand):
    help = 'Create initial data for authors'

    def handle(self, *args, **options):
        authors_data = [
            {
                'name': 'Guido van Rossum',
                'birth_date': date(1956, 1, 31),
            },
            {
                'name': 'James Gosling',
                'birth_date': date(1955, 5, 19),
            },
            {
                'name': 'Bjarne Stroustrup',
                'birth_date': date(1950, 12, 30),
            },
            {
                'name': 'Dennis Ritchie',
                'birth_date': date(1941, 9, 9),
            },
            {
                'name': 'Ken Thompson',
                'birth_date': date(1943, 2, 4),
            },
            {
                'name': 'Rasmus Lerdorf',
                'birth_date': date(1968, 11, 22),
            },
            {
                'name': 'Yukihiro Matsumoto',
                'birth_date': date(1965, 4, 14),
            },
            {
                'name': 'John McCarthy',
                'birth_date': date(1927, 9, 4),
            },
            {
                'name': 'Don Syme',
                'birth_date': date(1966, 12, 13),
            },
            {
                'name': 'Anders Hejlsberg',
                'birth_date': date(1960, 12, 2),
            },
        ]

        for author_data in authors_data:
            Author.objects.create(**author_data)

        self.stdout.write(self.style.SUCCESS('Successfully created authors'))