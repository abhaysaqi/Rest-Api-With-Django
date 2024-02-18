from django.urls import path
from .views import Movie_Api_View,MovieDetail

urlpatterns = [
    path('',Movie_Api_View.as_view()),
    path('<int:pk>/',MovieDetail.as_view())
]
