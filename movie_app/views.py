from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Min, Max, Count, Avg, Value


# Create your views here.

def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True))
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        new_budget=F('budget') + 100,
    )

    agg = Movie.objects.all().aggregate(Sum('budget'), Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
    })

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie,
    })