    # Rockstart Steve's Coming of Age Jukebox
    #### Video Demo:  https://youtu.be/zc1A0DOT2Wc?si=FHr4bMu3HRVjoiol
    #### Description:

    # Background
    I've always had success to read a syllabus ahead of courses and especially focus on the final project requirements.  I do this so that I can brainstorm during the course what I might want to do for my final project and start as early as possible and continue to build during the course.  When CS50P was learning about figlet and we "figletized" some text, I loved it.  For some reason, this was an inspiration along with the iTunes API.  That is when I put together an idea to honor my late brother in law Steve and create Rockstar Steve's Coming of Age Jukebox.  My idea was to ask a user for their age, calculate the decasde they would have attended High School and then utilize the iTunes API.

    As I set out to further implement the idea, I wondered how to query the iTunes API for songs during that decade.  Some considerations were to ask the user for their genre and then try to come up with a list of genre specific songs during those four years.  I ended up scraping this one after remembering that iTunes has Essential "Hits" lists for each decade. I used to listen to 70's to get in touch with songs during the decade I was born; having been born in 1975.

    That is when I settled on getting the users's age and base the search on iTunes Hits during the decade they attended High School.  I wanted to provide some sort of function of "picking" out songs which was when I decided to go with the randomizer and generate from the JSON return random 20 songs.

    ## Walking through the code:

    Note - you need to execute the following to install third party requests and figlet
    pip install requests
    pip install pyfiglet

    ### The code starts with the necessary import statements.
    import requests - imports the requests module so that you can access the iTunes API
    import sys - imports the built in sys module so that sys.exit can be called to exit the code gracefully
    import random - imports the build in random module necessary to randomize the songs from the iTunes API
    from pyfiglet import Figlet - imports the figlet class from the pyfiglet module

        import requests
        import sys
        import random
        from pyfiglet import Figlet

    Next, I created a main function.  The main function defines main with def main() and then inputs the ages name of the user with:

            def main():
                name = input("What is your name? ").title()

    Next, from main, I called the figletized function and figletized a greeting personalized to their name captured with input.
                figletized(f"{name}, Welcome to Rockstar Steve's Coming of Age Jukebox!")

    Then I called two more functions to both calculate the decade they attended high school and to search iTunes for the songs to randomize from the Hit List of that decade.

                decade = get_high_school_years(name)
                search_itunes(decade)

    First, the get_high_school_years(name) is executed passing in variable name from main.   Next a loop was created to either accpet an age 18 or older, or use the sys module to exit gracefully wiht a message "Sorry, this jukebox is for high sbhool grads only.  The text also makes use of calling the figletized function to slant figlative the text.

            def get_high_school_years(name):  # Assumes you are 18 years or older
                try:
                    age = int(input("What is your age? "))
                except ValueError:
                    sys.exit("Invaid input.  Please enter your age as a number.")

                if age < 18:
                    figletized(f"Sorry, {name}, this jukebox is for high school grads only")
                    sys.exit("Come back when you are 18 or older.")

    After the user successfully enters an age > 18, the calculate_grad_decade function is called which will then calculate and return the grad.  This is done by taking the age variable, in my case 50, and then the current year which is hard coded in as 2025.  A simple calculation naming the variable grad to calculate 2025 - 50-18 which results in 1993. Then a variable decade is assigned to value of grad which is 1993 divided by 10 which is 199.3, the // will dismiss the remainder resulting in 199 multiplied by 10 which yeilds 1990.  The code then calls figletized to tell the user in figletized slant that they must have graduated around (grad) in my case 1993, and were coming of age to (decade), in my case 1990 music. Finaly, grad and decade are returned.

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

    Now main calls search_itunes function passing the decade variable.  The url is used to generate_itunes_url passing in decade from above, in my case it is 1990. using the documentation from requests, the format is used for response = requests.get(url) and response.rasie_for_status() to check that the site is callable.  variable data is defined as response.json to store the response as a JSON return and sets up the results into data.get("results", []) which is a list, hence the [].  This JSON list in [] for results which is passed in the data variable, can now be selected calling the random module with selected = reandom.sample and selecting min(20) to set the size of the return and len(results) or length of results.
            def search_itunes(decade,):  # utilizes iTunes "Hits Essentials" playlists to random playlist
                url = generate_itunes_url(decade)
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                results = data.get("results", [])
                selected = random.sample(results, min(20, len(results)))  # returns list of 20 songs

    Next, this list of 20 songs is displayed to the user wiht print uderlined with \033 using the literal decade variable with an f string.
                print(f"\033[4m{decade}'s Recommended Playlist!\033[0m]")
                print()

    A loop is setup for the data in the JSON to capture the artist and the trackname and print these with the number in the list 1-20.
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

