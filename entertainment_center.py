import media
import fresh_tomatoes

# media descriptions stored in variables
baltoDesc = "Balto is a 1995 American animated epic drama adventure film directed by Simon Wells, produced by Amblin Entertainment and distributed by Universal Pictures. The film is loosely based on a true story about the dog of the same name who helped save children from the diphtheria epidemic in the 1925 serum run to Nome. The live-action portions of the film were shot at Central Park in New York City. The film was the third and final animated feature produced by Steven Spielberg's Amblimation animation studio. Spielberg, Kathleen Kennedy and Bonne Radford acted as executive producers on the film. Although the film's theatrical run was overshadowed by the success of the competing Pixar film Toy Story, its subsequent strong sales on home video led to two direct-to-video sequels: Balto II: Wolf Quest (2000) and Balto III: Wings of Change (2004) though none of the voice cast reprised their roles.[3][4]"

incDesc = "Inception is a 2010 science fiction film written, co-produced, and directed by Christopher Nolan, and co-produced by Emma Thomas. The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious, and is offered a chance to have his criminal history erased as payment for a seemingly impossible task: 'inception', the implantation of another person's idea into a target's subconscious.[4] The ensemble cast additionally includes Ken Watanabe, Joseph Gordon-Levitt, Marion Cotillard, Ellen Page, Tom Hardy, Dileep Rao, Cillian Murphy, Tom Berenger, and Michael Caine."

intDesc = "Interstellar is a 2014 epic science fiction film directed, co-written and co-produced by Christopher Nolan. The movie stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Casey Affleck, Ellen Burstyn, John Lithgow and Michael Caine. Set in a dystopian future where humanity is struggling to survive, it follows a group of astronauts who travel through a wormhole in search of a new home for humanity."

bmDesc = "Black Mirror is a British science fiction television anthology series created by Charlie Brooker. It centres around dark and satirical themes that examine modern society, particularly with regard to the unanticipated consequences of new technologies.[1] Episodes are standalone works, usually set in an alternative present or the near future. The show was first broadcast on the British Channel 4, in December 2011. A second series ran during February 2013. Then, in September 2015, Netflix commissioned a third series of 12 episodes, released in 2016.[2] The commissioned episodes were later divided into two series of six episodes. The third series was released on Netflix worldwide on 21 October 2016. Filming for the fourth series concluded in June 2017,[3] with the premiere expected later the same year.[4]"

willDesc = "Will & Grace is an American sitcom created by Max Mutchnick and David Kohan. Set in New York City, the show focuses on the relationship between best friends Will Truman (Eric McCormack), a gay lawyer, and Grace Adler (Debra Messing), a straight interior designer. The show was broadcast on NBC from September 21, 1998 to May 18, 2006, for a total of eight seasons, and restarted its run on NBC on September 28, 2017. During its original run, Will & Grace was one of the most successful television series with gay principal characters.[2]"

unbreakable = "Unbreakable Kimmy Schmidt is an American television sitcom created by Tina Fey and Robert Carlock, starring Ellie Kemper in the title role, that has streamed on Netflix since March 6, 2015.[1] Originally set for a 13-episode first season on NBC for spring 2015, the show was sold to Netflix and given a two-season order.[2]"

# created media objects with corresponding attributes
Balto = media.Movie("Balto", "77 minutes", baltoDesc, "https://upload.wikimedia.org/wikipedia/en/4/48/Balto_movie_poster.jpg", "https://www.youtube.com/watch?v=a6lGULmQdb0")

Inception = media.Movie("Inception", "148 minutes", incDesc, "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=66TuSJo4dZM")

Interstellar = media.Movie("Interstellar", "169 minutes", intDesc, "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=0vxOhd4qlnA")

BlackMirror = media.TvShow("Black Mirror", bmDesc, "http://cdn.collider.com/wp-content/uploads/2016/09/black-mirror-season-3-poster.png", "https://www.youtube.com/watch?v=jROLrhQkK78")

WillAndGrace = media.TvShow("Will and Grace", willDesc, "https://media.globaltv.com/uploadedimages/pages/shows/will_and_grace/will_and_grace_smartforms/willandgrace-logo.png", "https://www.youtube.com/watch?v=tkGn3l8wdG4")

Unbreakable = media.TvShow("Unbreakable", unbreakable, "https://www.shescribes.com/wp-content/uploads/2015/03/unbre_key_002_h.jpg", "https://www.youtube.com/watch?v=mNKEKlXY3Z4")

# calls the open_movies_page() method created in the fresh_tomatoes.py file that renders the html file for the website.
movies = [Balto, Inception, Interstellar]
tvshows = [BlackMirror, WillAndGrace, Unbreakable]
fresh_tomatoes.open_movies_page(movies, tvshows)
