import pandas as pd
from django.core.management.base import BaseCommand
from movies.models import Movie  # Replace 'movies' with your app name

class Command(BaseCommand):
    help = 'Import movies from a CSV file into the database'

    def handle(self, *args, **kwargs):
        # Path to your CSV file
        csv_file_path = r"C:\Users\Nithish S\Desktop\CSV\Top_1000_IMDb_movies_New_version.csv"

        # Load the dataset using Pandas
        df = pd.read_csv(csv_file_path)

        # Clean and convert data types as needed
        df['Gross'] = df['Gross'].replace({r'\$': '', ',': ''}, regex=True).astype(str).replace({'#222': '0', '': '0'}).astype(float)
        df['Votes'] = df['Votes'].replace({',': ''}, regex=True).astype(str).replace({'#222': '0', '': '0'}).astype(int)
        df['Metascore of movie'] = df['Metascore of movie'].replace({'': '0'}).astype(float)

        # Handle NaN values
        df['Gross'] = df['Gross'].fillna(0)
        df['Votes'] = df['Votes'].fillna(0)
        df['Metascore of movie'] = df['Metascore of movie'].fillna(0)

        # Clean year_of_release column
        df['Year of Release'] = pd.to_numeric(df['Year of Release'], errors='coerce').fillna(0).astype(int)

        # Iterate over the DataFrame rows and create Movie objects
        for _, row in df.iterrows():
            # Skip rows where year_of_release is 0 (invalid)
            if row['Year of Release'] == 0:
                continue

            movie, created = Movie.objects.get_or_create(
                movie_name=row['Movie Name'],
                year_of_release=row['Year of Release'],
                watch_time=row['Watch Time'],
                movie_rating=row['Movie Rating'],
                metascore=row['Metascore of movie'],
                gross=row['Gross'],
                votes=row['Votes'],
                description=row['Description']
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added movie: {movie.movie_name}'))

        self.stdout.write(self.style.SUCCESS('Movies imported successfully!'))
