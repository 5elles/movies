from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show_all_movie),
    path('directors', views.Directors_View.as_view()),
    path('directors/<int:id_director>', views.show_one_director, name='director-detail'),
    path('actors', views.actors_View.as_view(), name='allActors-detail'),
    path('actors/<int:id_actor>', views.show_one_actor, name='actor-detail'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail')
]