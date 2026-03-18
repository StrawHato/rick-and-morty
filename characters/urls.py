from django.urls import path

from characters.views import get_random_character_view, CharacterListView

urlpatterns = [
    path("random", get_random_character_view, name="random-character"),
    path("", CharacterListView.as_view(), name="character-list"),
]

app_name = "characters"
