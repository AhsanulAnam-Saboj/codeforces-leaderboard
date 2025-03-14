# Generated by Django 5.1.7 on 2025-03-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeforcesUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('handle', models.CharField(max_length=50, unique=True)),
                ('address', models.TextField()),
                ('batch', models.TextField()),
                ('session', models.CharField(max_length=20)),
                ('roll_number', models.CharField(max_length=20)),
                ('current_rating', models.IntegerField(null=True)),
                ('max_rating', models.IntegerField(null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
