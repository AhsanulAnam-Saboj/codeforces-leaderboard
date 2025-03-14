from django.urls import path
from .views import LeaderboardListView, LeaderboardDetailView

urlpatterns = [
    path('leaderboard/', LeaderboardListView.as_view(), name='leaderboard_list'),  # List and create users
    path('leaderboard/<int:pk>/', LeaderboardDetailView.as_view(), name='leaderboard_detail'),  # Get, update, delete a user
]
