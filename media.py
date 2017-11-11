# Defines a class Movie


class Movie():
    def __init__(self, movie_title, poster_image_url, youtube_trailer_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = youtube_trailer_url

# Defines a class TvShow


class TvShow():
    def __init__(self, show_title, show_poster, youtube_trailer_url):
        self.title = show_title
        self.poster_image_url = show_poster
        self.trailer_youtube_url = youtube_trailer_url
