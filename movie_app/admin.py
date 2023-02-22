from django.contrib import admin
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet


# Register your models here.
admin.site.register(Actor)  # второй способ регистрации - декоратор @admin.register(НазвМодели)
# admin.site.register(DressingRoom)

@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):
    title = "Фильтр по рейтингу"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>= 80', 'Высочайший'),
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>= 80':
            return queryset.filter(rating__gte=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (('name', 'year', 'rating'), ('budget', 'currency'), 'description', 'director', 'actors', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "rating", "year", "budget", "director", "rating_status"]
    list_editable = ["rating", "year", "budget", "director"]
    filter_horizontal = ["actors"]
    ordering = ["name"]
    list_per_page = 10
    actions = ["set_dollars", "set_euros", "set_rubles"]
    search_fields = ['name', 'rating']
    list_filter = ["currency", RatingFilter]

    @admin.display(ordering='rating', description='status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в USD')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в EUR')
    def set_euros(self, request, qs: QuerySet):
        qs.update(currency=Movie.EURO)

    @admin.action(description='Установить валюту в RUB')
    def set_rubles(self, request, qs: QuerySet):
        count = qs.update(currency=Movie.RUR)
        self.message_user(request, f'Изменено записей: {count}')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    fields = [('first_name', 'patronymic'), 'last_name', 'director_email']

