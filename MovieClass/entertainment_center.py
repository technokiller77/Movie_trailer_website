import media
import fresh_tomatoes

avengers = media.Movie("Avngers",
                       "A group of superheroes unite to fight of strong villians",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# print(avengers.storyline)

lotr = media.Movie("LOTR: The Fellowship of the Ring",
                   "A group of 9 from different races join together to destroy the ring of the Dark Lord",
                   "https://goo.gl/h1guWm",
                   "https://www.youtube.com/watch?v=V75dMMIW2B4")

bugs_life = media.Movie("A bug's Life",
                        "Storyline",
                        "https://goo.gl/N9Co3g",
                        "https://www.youtube.com/watch?v=5j1m2wwdcVA")

interstellar = media.Movie("Interstellar",
                           "storyline",
                           "https://goo.gl/pDVNBG",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

inception = media.Movie("Inception",
                        "Storyline",
                        "https://goo.gl/UBRCe9",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0&t=5s")

pianist = media.Movie("The Pianist",
                      "storyline",
                      "https://goo.gl/eLruDR",
                      "https://www.youtube.com/watch?v=BFwGqLa_oAo")

movies = [lotr, interstellar, inception, pianist]
# fresh_tomatoes.open_movies_page(movies)

# print(lotr.storyline)
# lotr.show_trailer()
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)







