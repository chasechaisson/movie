import media 
import fresh_tomatoes

baltoDesc = "Balto is a 1995 American animated epic drama adventure film directed by Simon Wells, produced by Amblin Entertainment and distributed by Universal Pictures. The film is loosely based on a true story about the dog of the same name who helped save children from the diphtheria epidemic in the 1925 serum run to Nome. The live-action portions of the film were shot at Central Park in New York City. The film was the third and final animated feature produced by Steven Spielberg's Amblimation animation studio. Spielberg, Kathleen Kennedy and Bonne Radford acted as executive producers on the film. Although the film's theatrical run was overshadowed by the success of the competing Pixar film Toy Story, its subsequent strong sales on home video led to two direct-to-video sequels: Balto II: Wolf Quest (2000) and Balto III: Wings of Change (2004) though none of the voice cast reprised their roles.[3][4]"

Balto = media.Movie("Balto", "77 mins", baltoDesc, "https://upload.wikimedia.org/wikipedia/en/4/48/Balto_movie_poster.jpg", "https://www.youtube.com/watch?v=a6lGULmQdb0")

movies = [Balto]
fresh_tomatoes.open_movies_page(movies)
