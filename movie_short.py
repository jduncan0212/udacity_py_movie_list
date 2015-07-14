import webbrowser

"""
    File:               media_short.py
    Imports:            webbrowser
    Defines Classes:    Movie:
                            A simple class describing a movie by using it's
                            title, a short summary, a poster image and
                            youtube trailer

"""


class Movie():
    """Define a Movie Class:
    class:              Movie
    description:        A simple class to describe a movie using its title,
                        youtube trailer, box art, and a short summary.
    data attributes:    The Movie's Title (movie_title), story summary
                        (story_summary), box art (poster_image) and trailer on
                        youtube (trailer_youtube).
    method attributes:  show_trailer:
                            method which shows the trailer on youtube.
    """

    def __init__(self, movie_title, story_summary,
                 poster_image, trailer_youtube):

        """
            __init__ constructor:
                takes required arguments:  movie_title, story_summary,
                                            poster_image, trailer_youtube
        """

        self.title = movie_title
        self.storyline = story_summary
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
            show_trailer method:    when called shows the trailer via opening a
                                    browser window
        """

        webbrowser.open(self.trailer_youtube)
