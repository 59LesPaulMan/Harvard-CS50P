import requests
import sys
import random
from pyfiglet import Figlet


def main():
    name = input("What is your name? ").title()
    figletized(f"{name}, Welcome to Rockstar Steve's Coming of Age Jukebox!")

    decade = get_high_school_years(name)
    search_itunes(decade)


def get_high_school_years(name):

    age = int(input("What is your age? "))
    year = 2025
    grad = int(year - (age - 18))
    decade = (grad // 10) * 10

    figletized(f"I see, {name}, you must have graduated around {grad},")
    figletized(f"and were coming of age to {decade}'s music!")
    return decade


def search_itunes(decade):
    search_decade = f"{str(decade)[-2:]}s Hits Essentials"
    url = f"https://itunes.apple.com/search?term={search_decade.replace(' ', '+')}&entity=song&limit=200"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    results = data.get("results", [])

    selected = random.sample(results, min(20, len(results)))

    print(f"\033[4m{decade}'s Recommended Playlist!\033[0m]")
    print()

    for i, song in enumerate(selected, 1):
        title = song.get("trackName", "Unknown Title")
        artist = song.get("artistName", "Unknown Artist")
        print(f"{i}. {title} - {artist}")


def figletized(text):
    f = Figlet(font="slant")
    print(f.renderText(text))


main()
