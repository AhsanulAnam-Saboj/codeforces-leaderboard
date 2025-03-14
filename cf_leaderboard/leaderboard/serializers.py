from rest_framework import serializers
from leaderboard.models import CodeforcesUser
from django.utils import timezone

class CodeforcesUserSerializer(serializers.Serializer):


    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    profile_picture = serializers.ImageField(required=False)
    handle = serializers.CharField(max_length=50)
    batch = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    session = serializers.CharField(max_length=20)
    roll_number = serializers.CharField(max_length=20)
    # Corrected allow_null usage here 👇
    current_rating = serializers.IntegerField(allow_null=True, required=False)
    max_rating = serializers.IntegerField(allow_null=True, required=False)

    last_updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """Create a new CodeforcesUser instance"""
        from leaderboard.utils import fetch_codeforces_rating  # Assuming you have a function for this
        
        handle = validated_data.get('handle')
        rating_data = fetch_codeforces_rating(handle)  # This fetches rating from Codeforces

        # Add rating to validated_data before saving
        validated_data['current_rating'] = rating_data
        validated_data['last_updated'] = timezone.now()

        return CodeforcesUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update an existing CodeforcesUser instance"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
