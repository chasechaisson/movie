import media 
import fresh_tomatoes

baltoDesc = "Balto is a 1995 American animated epic drama adventure film directed by Simon Wells, produced by Amblin Entertainment and distributed by Universal Pictures. The film is loosely based on a true story about the dog of the same name who helped save children from the diphtheria epidemic in the 1925 serum run to Nome. The live-action portions of the film were shot at Central Park in New York City. The film was the third and final animated feature produced by Steven Spielberg's Amblimation animation studio. Spielberg, Kathleen Kennedy and Bonne Radford acted as executive producers on the film. Although the film's theatrical run was overshadowed by the success of the competing Pixar film Toy Story, its subsequent strong sales on home video led to two direct-to-video sequels: Balto II: Wolf Quest (2000) and Balto III: Wings of Change (2004) though none of the voice cast reprised their roles.[3][4]"

incDesc = "Inception is a 2010 science fiction film written, co-produced, and directed by Christopher Nolan, and co-produced by Emma Thomas. The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious, and is offered a chance to have his criminal history erased as payment for a seemingly impossible task: 'inception', the implantation of another person's idea into a target's subconscious.[4] The ensemble cast additionally includes Ken Watanabe, Joseph Gordon-Levitt, Marion Cotillard, Ellen Page, Tom Hardy, Dileep Rao, Cillian Murphy, Tom Berenger, and Michael Caine."

intDesc = "Interstellar is a 2014 epic science fiction film directed, co-written and co-produced by Christopher Nolan. The movie stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Casey Affleck, Ellen Burstyn, John Lithgow and Michael Caine. Set in a dystopian future where humanity is struggling to survive, it follows a group of astronauts who travel through a wormhole in search of a new home for humanity."

bmDesc = "Black Mirror is a British science fiction television anthology series created by Charlie Brooker. It centres around dark and satirical themes that examine modern society, particularly with regard to the unanticipated consequences of new technologies.[1] Episodes are standalone works, usually set in an alternative present or the near future. The show was first broadcast on the British Channel 4, in December 2011. A second series ran during February 2013. Then, in September 2015, Netflix commissioned a third series of 12 episodes, released in 2016.[2] The commissioned episodes were later divided into two series of six episodes. The third series was released on Netflix worldwide on 21 October 2016. Filming for the fourth series concluded in June 2017,[3] with the premiere expected later the same year.[4]"

Balto = media.Movie("Balto", "77 minutes", baltoDesc, "https://upload.wikimedia.org/wikipedia/en/4/48/Balto_movie_poster.jpg", "https://www.youtube.com/watch?v=a6lGULmQdb0")

Inception = media.Movie("Inception", "148 minutes", incDesc, "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=66TuSJo4dZM")

Interstellar = media.Movie("Interstellar", "169 minutes", intDesc, "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=0vxOhd4qlnA")

BlackMirror = media.TvShow("Black Mirror", bmDesc, "http://cdn.collider.com/wp-content/uploads/2016/09/black-mirror-season-3-poster.png", "https://www.youtube.com/watch?v=jROLrhQkK78")

movies = [Balto, Inception, Interstellar]
tvshows = [BlackMirror]
fresh_tomatoes.open_movies_page(movies, tvshows)