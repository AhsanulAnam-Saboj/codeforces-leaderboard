from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from leaderboard.models import CodeforcesUser
from leaderboard.serializers import CodeforcesUserSerializer
from .utils import fetch_codeforces_rating

class LeaderboardListView(APIView):
    """Handles GET and POST requests for the leaderboard"""

    def get(self, request):
        """Retrieve all users, update their ratings, and return sorted list"""
        # Fetch all users and update their ratings
        users = CodeforcesUser.objects.all()
        for user in users:
            new_rating = fetch_codeforces_rating(user.handle)
            if new_rating is not None and new_rating != user.current_rating:
                user.current_rating = new_rating['current_rating']
                user.max_rating = new_rating['max_rating']
                user.save()

        # Serialize the users data and return as response
        users = CodeforcesUser.objects.all().order_by('-max_rating')
        serializer = CodeforcesUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new user and fetch their rating from Codeforces"""
        # Deserialize the incoming data
        print(request.data)
        serializer = CodeforcesUserSerializer(data=request.data)
        
        print(request.FILES)
        if serializer.is_valid():
            # Get the Codeforces handle from the data
            handle = serializer.validated_data['handle']
            rating = fetch_codeforces_rating(handle)
            print(f"Rating = {rating}")
            if rating is None:
                return Response({'error': 'Invalid Codeforces handle or failed to fetch rating'}, status=status.HTTP_400_BAD_REQUEST)

            # Set default values for current_rating and max_rating
            user_data = serializer.validated_data
            user_data['current_rating'] = rating.get('current_rating', None)
            user_data['max_rating'] = rating.get('max_rating', None) # Or any other logic you need to set here

            profile_picture = request.FILES.get('profile_picture', None)
            if profile_picture:
             user_data['profile_picture'] = profile_picture
            # Save the user instance with the updated data
            user = CodeforcesUser.objects.create(**user_data)

            return Response(CodeforcesUserSerializer(user).data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeaderboardDetailView(APIView):
    """Handles GET, PUT, and DELETE requests for a specific user"""

    def get(self, request, pk):
        """Retrieve a single user by their ID"""
        try:
            user = CodeforcesUser.objects.get(pk=pk)
        except CodeforcesUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CodeforcesUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a specific user's information"""
        try:
            user = CodeforcesUser.objects.get(pk=pk)
        except CodeforcesUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CodeforcesUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a specific user"""
        try:
            user = CodeforcesUser.objects.get(pk=pk)
        except CodeforcesUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
