from django.contrib import admin

# Register your models here.
from .models import CodeforcesUser  # Import your model

# Register the model
admin.site.register(CodeforcesUser)