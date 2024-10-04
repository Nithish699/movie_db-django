# Generated by Django 5.0.6 on 2024-08-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=255)),
                ('year_of_release', models.IntegerField()),
                ('watch_time', models.IntegerField()),
                ('movie_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('metascore', models.IntegerField()),
                ('gross', models.DecimalField(decimal_places=2, max_digits=10)),
                ('votes', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Credit',
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='MovieMetadata',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
