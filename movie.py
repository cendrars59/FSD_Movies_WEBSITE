
# dependencies import 
import webbrowser

class Movie (): 

	""" Class documentation 

	This class includes an init method def __init__
	This class includes an method show_trailer() passing self as argument

	"""

	# Init method in order to instances of Movie Class 
	def __init__(self, title, description, trailer_youtube_url, poster_image_url) :
		
		self.title = title 
		self.description = description 
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_image_url

	# Method in order to disp^lay the trailer of the movie 	
	def show_trailer(self) :

		webbrowser.open(self.trailer_youtube_url)
