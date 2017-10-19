"""Defines a class Movie that takes in and stores attributes for movie objects when created"""
class Movie():
	def __init__(self, movie_title, movie_duration, movie_storyline, poster_image_url, youtube_trailer_url):
		self.title = movie_title
		self.duration = movie_duration
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = youtube_trailer_url

"""Defines a class TvShow that takes in and stores attributes for tvshow objects when created"""
class TvShow():
	def __init__(self, show_title, show_description, show_poster, youtube_trailer_url):
		self.title = show_title
		self.description = show_description
		self.poster_image_url = show_poster
		self.trailer_youtube_url = youtube_trailer_url