import movie_short
import fresh_tomatoes


# I made the design choice to add each movie into a dict instead of a list, and then
# convert to a list later on.
#
# My reasoning was that a dict is a more convient structure to access a particular movie
# should we ever have the need to in the future.

all_movies = {}

# used to populate the dict: all_movies
def add_to_dict(movie):
    all_movies[movie.title] = movie
    return

toy_story = movie_short.Movie("Toy Story",
                              "What do toys do when you're away?",
                              "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                              "https://www.youtube.com/watch?v=KYz2wyBy3kc")

add_to_dict(toy_story)


star_wars_a_new_hope = movie_short.Movie("Star Wars: A New Hope", "A long time ago, in a galaxy far, far away....\n"+
                             " It is a period of civil war. ",
                             "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                             "https://www.youtube.com/watch?v=1g3_CFmnU7k")
add_to_dict(star_wars_a_new_hope)


#I had to use the opening scene as sony has blocked the trailer, for the various youtube urls I found
godfather_i = movie_short.Movie("The Godfather", "A story of the Mafia Corleone Family in New York City",
                             "http://www.faithmeetsworld.com/wp-content/uploads/2014/05/Godfather.jpg",                               
                             "https://www.youtube.com/watch?v=OIBpHO1gZgQ")

add_to_dict(godfather_i)


nausicaa = movie_short.Movie("Nausicaa of the Valley of the Wind", "In a Post-Apocalyptic Earth,"+
                             " a young heroine seeks to save her country...",
                             "https://upload.wikimedia.org/wikipedia/en/b/bc/Nausicaaposter.jpg",
                             "https://www.youtube.com/watch?v=vJdQtnhKAtU")
add_to_dict(nausicaa)



voices_from_the_shadows = movie_short.Movie("Voices from the Shadows", "A documentary on the illness Myalgic Encephalomyelitis"+
                             " and the rampant denialism in the medical and research professions",
                             "http://voicesfromtheshadowsfilm.co.uk/wpress/wp-content/uploads/2012/01/New-dvd-cover-front.jpg",
                             "https://www.youtube.com/watch?v=fiuqTx0u-Yw")

add_to_dict(voices_from_the_shadows)

spartacus = movie_short.Movie("Spartacus", "A slave rebellion in Ancient Republican Rome ends with "+
                             "...a moral victory?",
                             "http://www.doctormacro.com/Images/Posters/S/Poster%20-%20Spartacus_02.jpg",
                             "https://www.youtube.com/watch?v=HcIMY1Ah3aw")

add_to_dict(spartacus)


#maybe I didn't like this movie after all...
"""kazaam = movie_short.Movie("Kazaam", "Shaquille O'Neal as a rapping genie"+
                             " ...what could go wrong?",
                             "https://upload.wikimedia.org/wikipedia/en/3/38/Kazaam_poster.jpg",
                             "https://www.youtube.com/watch?v=ZA9AtHjJxWM")

add_to_dict(kazaam)"""

emperors_club = movie_short.Movie("The Emperor's Club", "A teacher attempts to teach a privileged"+
                             " student lessons in morality.",
                             "https://upload.wikimedia.org/wikipedia/en/5/58/The_Emperor%27s_Club_Poster.jpg",
                             "https://www.youtube.com/watch?v=k0gHibeHfdA")

add_to_dict(emperors_club)

fellowship_of_the_ring = movie_short.Movie("The Fellowship of the Ring", "A young hobbit inherits a powerful, dangerous"+
                             " magic ring.",
                             "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
                             "https://www.youtube.com/watch?v=V75dMMIW2B4")

add_to_dict(fellowship_of_the_ring)


good_will_hunting = movie_short.Movie("Good Will Hunting", "A smartest person at MIT is the janitor",
                             "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                             "https://www.youtube.com/watch?v=PaZVjZEFkRs")

add_to_dict(good_will_hunting)

#open movies html page
fresh_tomatoes.open_movies_page([all_movies[key] for key in all_movies.keys()], all_movies)

