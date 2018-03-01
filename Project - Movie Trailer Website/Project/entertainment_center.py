import media
import fresh_tomatoes

# Creating instances based on the class Movie.

avengers_infinity_war = media.Movie("Avengers: Infinity War", "The Avengers and their allies must defeat the powerful Thanos",
                                    "http://bit.ly/2AQVyKc", "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

the_incredibles_2 = media.Movie("The Incredibles 2", "Bob Parr (Mr. Incredible) is left to care for Jack-Jack while Helen (Elastigirl) is out saving the world.",
                                "http://bit.ly/2Csh2CD", "https://www.youtube.com/watch?v=X6waHtSgCTc")

mission_impossible = media.Movie("Mission: Impossible - Fallout", "Ethan Hunt and his IMF team, race against time after a mission gone wrong.",
                                 "http://bit.ly/2F9hW7T", "https://www.youtube.com/watch?v=wb49-oV0F78")
    
red_sparrow = media.Movie("Red Sparrow", "Ballerina Dominika Egorova is recruited to 'Sparrow School,' where she is forced to use her body as a weapon.",
                          "http://bit.ly/2F1vX4t", "https://www.youtube.com/watch?v=PmUL6wMpMWw")

annihilation = media.Movie("Annihilation", "A biologist signs up for a dangerous, secret expedition where the laws of nature don't apply.",
                         "http://bit.ly/2CNJ7A3", "https://www.youtube.com/watch?v=89OP78l9oF0")

pacific_rim_uprising = media.Movie("Pacific Rim: Uprising", "Jake Pentecost reunites with Mako Mori to lead a new generation of Jaeger pilots, against a new Kaiju.",
                                   "http://bit.ly/2Cry2J0", "https://www.youtube.com/watch?v=8BAhwgjMvnM")


# Transfering objects to a list.
movies = [avengers_infinity_war, the_incredibles_2, mission_impossible, red_sparrow, annihilation, pacific_rim_uprising]


# Calling the function that opens the website.
fresh_tomatoes.open_movies_page(movies)



