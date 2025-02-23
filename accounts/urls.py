from django.urls import path
from accounts.views import UserListCreateView, ProfileDetailView, ProfileListCreateView

urlpatterns = [
    path('users/',UserListCreateView.as_view(), name='user-list-create'),
    path('profile/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profile/<int:pk>', ProfileDetailView.as_view(),name='profle-detail')
]
