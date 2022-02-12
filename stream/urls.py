from . import views
from . views import (
    VideoDetailView, 
    UserVideoListView, 
    VideoCreateView, 
    GeneralVideoListView, 
    VideoUpdateView,
    VideoDeleteView,
)
from django.urls import path 


app_name = "stream"

urlpatterns = [
    path('',GeneralVideoListView.as_view(), name="video-list"),
    path('video/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name="video-update"),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name="video-delete"),
    path('user/<str:username>', UserVideoListView.as_view(), name="user-videos"),
    path('video/new/',VideoCreateView.as_view(), name="video-create"),
    path('search',views.search,name="search"),
]


