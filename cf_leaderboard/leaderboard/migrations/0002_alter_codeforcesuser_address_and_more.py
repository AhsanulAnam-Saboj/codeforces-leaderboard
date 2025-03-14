# Generated by Django 5.1.7 on 2025-03-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeforcesuser',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='codeforcesuser',
            name='batch',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='codeforcesuser',
            name='current_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='codeforcesuser',
            name='max_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
