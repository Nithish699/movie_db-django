# Generated by Django 5.0.6 on 2024-08-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cast', models.TextField(null=True)),
                ('crew', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('keywords', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('movieId', models.IntegerField(primary_key=True, serialize=False)),
                ('imdbId', models.IntegerField(null=True)),
                ('tmdbId', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieMetadata',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('adult', models.BooleanField(default=False)),
                ('belongs_to_collection', models.TextField(null=True)),
                ('budget', models.BigIntegerField(null=True)),
                ('genres', models.TextField(null=True)),
                ('homepage', models.URLField(null=True)),
                ('imdb_id', models.CharField(max_length=15, null=True)),
                ('original_language', models.CharField(max_length=10, null=True)),
                ('original_title', models.CharField(max_length=255, null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.CharField(max_length=255, null=True)),
                ('production_companies', models.TextField(null=True)),
                ('production_countries', models.TextField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('revenue', models.BigIntegerField(null=True)),
                ('runtime', models.FloatField(null=True)),
                ('spoken_languages', models.TextField(null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('tagline', models.TextField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('video', models.BooleanField(default=False)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('movieId', models.IntegerField()),
                ('rating', models.FloatField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
