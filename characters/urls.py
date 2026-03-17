from django.urls import path

from characters.views import get_random_character_view

urlpatterns = [
    path("random", get_random_character_view, name="random-character"),
]

app_name = "characters"
