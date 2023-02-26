from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show_all_movie),
    path('directors', views.Directors_View.as_view()),
    path('director/<int:pk>', views.OneDirectorView.as_view(), name='director-detail'),
    path('actors', views.actors_View.as_view(), name='allActors-detail'),
    path('actor/<int:pk>', views.OneActorView.as_view(), name='actor-detail'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail')
]