# Generated by Django 5.1.7 on 2025-03-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_alter_codeforcesuser_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeforcesuser',
            name='current_rating',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='codeforcesuser',
            name='max_rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
