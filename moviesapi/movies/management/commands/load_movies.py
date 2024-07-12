import pandas as pd
from django.core.management.base import BaseCommand
from movies.models import Movie


class Command(BaseCommand):
    help = 'Load movies data from CSV file into the database'

    def handle(self, *args, **kwargs):
        df = pd.read_csv('D:/vphrase/new_movies.csv')
        for _, row in df.iterrows():
            Movie.objects.create(
                movies=row['MOVIES'],
                year=row['YEAR'],
                genre=row['GENRE'],
                rating=row['RATING'],
                oneline=row['ONE-LINE'],
                stars=row['STARS'],
                votes=row['VOTES'],
                runtime=row['RunTime'],
                gross=row['Gross']
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
