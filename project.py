# RockStar Steve's Coming of Age Jukebox is dedicated to my late brother in law Rockstar Steve
# The code prompts the user for their age, calculates their high school decade,
# then fetches a randomized music playlist form the iTunes API.

import requests
import sys
import random
from pyfiglet import Figlet


def main():
    name = input("What is your name? ").title()
    figletized(f"{name}, Welcome to Rockstar Steve's Coming of Age Jukebox!")
    decade = get_high_school_years(name)
    search_itunes(decade)


def get_high_school_years(name):  # Assumes you are 18 years or older
    try:
        age = int(input("What is your age? "))
    except ValueError:
        sys.exit("Invaid input.  Please enter your age as a number.")

    if age < 18:
        figletized(f"Sorry, {name}, this jukebox is for high school grads only")
        sys.exit("Come back when you are 18 or older.")

    grad, decade = calculate_grad_decade(age)
    figletized(f"I see, {name}, you must have graduated around {grad},")
    figletized(f"and were coming of age to {decade}'s music!")
    return decade


def calculate_grad_decade(
    age, current_year=2025
):  # hardcoded 2025 year to calculate decade
    grad = int(current_year - (age - 18))
    decade = (grad // 10) * 10
    return grad, decade


def search_itunes(
    decade,
):  # utilizes iTunes "Hits Essentials" playlists to random playlist
    url = generate_itunes_url(decade)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    results = data.get("results", [])
    selected = random.sample(results, min(20, len(results)))  # returns list of 20 songs

    print(f"\033[4m{decade}'s Recommended Playlist!\033[0m]")
    print()

    for i, song in enumerate(selected, 1):
        title = song.get("trackName", "Unknown Title")
        artist = song.get("artistName", "Unknown Artist")
        print(f"{i}. {title} - {artist}")


def generate_itunes_url(
    decade,
):  # construct search URL for iTunes API using decade-based hits playlist
    search_decade = f"{str(decade)[-2:]}s Hits Essentials"
    return f"https://itunes.apple.com/search?term={search_decade.replace(' ', '+')}&entity=song&limit=200"  # limits return of 200 to JSON


def figletized(text):  # can be called to figletize any text
    f = Figlet(font="slant")
    print(f.renderText(text))


if __name__ == "__main__":

    main()
