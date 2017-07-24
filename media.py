class Movie():
    """
    This class provides a way to
    store your favorate movies'
    related information
    """

    def __init__(
        self, movie_title, movie_storyline, poster_image, trailer_youtube
    ):
        """Constructor for Movie class

        Keyword arguments:
        movie_title -- the movie's name
        movie_storyline -- the brief content of the movie
        poster_image -- the url of the movie poster
        trailer_youtube -- the youtube url of the movie trailer
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
