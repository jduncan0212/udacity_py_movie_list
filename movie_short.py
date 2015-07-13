import webbrowser

class Movie():
    def __init__(self, movie_title, story_summary,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = story_summary
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
    
