from django.shortcuts import render
from rest_framework import generics
from myapp.models import Movie
from .serializers import MovieSerializer
# Create your views here.
class Movie_Api_View(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
