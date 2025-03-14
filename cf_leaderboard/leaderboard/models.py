from django.db import models

class CodeforcesUser(models.Model):
    
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Requires MEDIA setup
    handle = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)  # Added max_length for better validation
    batch = models.CharField(max_length=50)     # Added max_length for consistency
    session = models.CharField(max_length=20)   # Example: "2020-2024"
    roll_number = models.CharField(max_length=20)
    current_rating = models.IntegerField(default=0)
    max_rating = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.handle}) - {self.current_rating}"
