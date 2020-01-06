from django.urls import path, include
from . import views
from .views import (
    HomePageView,

)


urlpatterns = [
    # path('', views.home, name='main-home'),
    path('', include('frontend.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('guide/', views.guide, name='guide'),
    # path('streams/', views.streams, name='streams'),
]
