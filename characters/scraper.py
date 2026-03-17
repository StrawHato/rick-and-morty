import requests
from django.conf import settings

from characters.models import Character


def scrape_characters() -> list[Character]:
    next_url_to_scrape = settings.RICK_AND_MORTY_API_CHARACTERS_URL

    characters = []
    while next_url_to_scrape is not None:
        characters_response = requests.get(next_url_to_scrape)
        characters_response.raise_for_status()

        data = characters_response.json()

        for character_dict in data["results"]:
            characters.append(
                Character(
                    name=character_dict["name"],
                    api_id=character_dict["id"],
                    status=character_dict["status"],
                    gender=character_dict["gender"],
                    species=character_dict["species"],
                    image=character_dict["image"],
                )
            )

        next_url_to_scrape = data["info"]["next"]

    return characters


def save_characters(characters: list[Character]):
    for character in characters:
        character.save()


def sync_characters_with_api():
    characters = scrape_characters()
    save_characters(characters)
