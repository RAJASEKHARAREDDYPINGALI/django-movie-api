from django.conf.urls import include, url

from api_framework.views import MovieListAPIView, MovieDetailAPIView, MovieCreateAPIView

urlpatterns = [
    url(r'^movie/$', MovieListAPIView.as_view(), name="movie_list_create_api_view"),
    url(r'^movie/create/$', MovieCreateAPIView.as_view(), name="movie_create_create_api_view"),

    url(r'^movie/(?P<pk>\d+)/$', MovieDetailAPIView.as_view(), name="movie_detail_api_view"),

]
