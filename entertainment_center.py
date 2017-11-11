import media
import fresh_tomatoes

# created media objects with corresponding attributes
Balto = media.Movie("Balto",
                    "https://upload.wikimedia.org/wikipedia/\
                    en/4/48/Balto_movie_poster.jpg",
                    "https://www.youtube.com/watch?v=nmcxtJTLe6k")

Inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/\
                        en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

Interstellar = media.Movie("Interstellar",
                           "https://upload.wikimedia.org/wikipedia/\
                            en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

BlackMirror = media.TvShow("Black Mirror",
                           "http://cdn.collider.com/wp-content/uploads/\
                            2016/09/black-mirror-season-3-poster.png",
                           "https://www.youtube.com/watch?v=jROLrhQkK78")

WillAndGrace = media.TvShow("Will and Grace",
                            "https://media.globaltv.com/uploadedimages/pages/\
                            shows/will_and_grace/will_and_grace_smartforms/\
                            willandgrace-logo.png",
                            "https://www.youtube.com/watch?v=tkGn3l8wdG4")

Unbreakable = media.TvShow("Unbreakable",
                           "https://www.shescribes.com/wp-content/uploads/\
                            2015/03/unbre_key_002_h.jpg",
                           "https://www.youtube.com/watch?v=mNKEKlXY3Z4")

# calls the open_movies_page() method
movies = [Balto, Inception, Interstellar]
tvshows = [BlackMirror, WillAndGrace, Unbreakable]
fresh_tomatoes.open_movies_page(movies, tvshows)
