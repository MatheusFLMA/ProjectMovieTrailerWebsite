# Module responsible for opening a webpage.
import webbrowser

# Creating the main class that will provide attributes and behaviors


class Movie():

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]   # This list will never change

    # Function that defines the necessary attributes.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """This function will be used for instantiation. The arguments will
        be stored inside methods that will be used by objects.

        Args:
            self: the object itself.
            movie_title: A string containing the movie's title.
            movie_sotoryline: Write few words about the movie's plot.
            poster_image: A string containing the URL of a poster.
            trailer_youtube: A string containing a URL from a
            YouTube video.

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function responsible for opening the trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
