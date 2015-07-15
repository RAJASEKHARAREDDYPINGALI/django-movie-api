from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework import serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse("movie_detail_api_view", kwargs={"pk": obj.pk})

    class Meta:
        model = Movie
        fields = ("title", "url", "funny")


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        print(request.user)
        return super().create(request, *args, **kwargs)


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
