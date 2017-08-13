import media
import fresh_tomatoes

# Memento movie: movie title, storyline, poster image and movie trailer
memento = media.Movie(
    "Memento (2000)",
    "A man juggles searching for his wife's murderer and keeping his"
    "short-term memory loss.",
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=zgd0-VttkmA"
    )

# The Dark Knight movie: movie title, storyline, poster image and movie trailer
the_dark_knight = media.Movie(
    "The Dark Knight (2008)",
    "The Dark Knight accepts the biggest physical and mental test to"
    "fight injustice.",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
    "https://www.youtube.com/watch?v=EXeTwQWrcwY"
    )

# Black Swan movie: movie title, storyline, poster image and movie trailer
black_swan = media.Movie(
    "Black Swan (2010)",
    "A dancing lead role winner only finds herself struggling to maintain"
    "her sanity.",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Black_Swan_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=YAAseAiOjnQ"
    )

# The Imitation Game movie: movie title, storyline, poster image, movie trailer
the_imitation_game = media.Movie(
    "The Imitation Game (2014)",
    "During World War II, mathematician Alan Turing tries to crack the"
    "enigma code.",
    "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=S5CjKEFb-sM"
    )

# Ex Machina movie: movie title, storyline, poster image and movie trailer
ex_machina = media.Movie(
    "Ex Machina (2014)",
    "A young programmer is selected to the experiment in synthetic"
    "intelligence.",
    "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=3hAlv0xLJJ4"
    )

# Kingsman movie: movie title, storyline, poster image and movie trailer
kingsman = media.Movie(
    "Kingsman (2014)",
    "A spy organization recruits a promising kid into the ultra-competitive"
    "programes.",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=hN0JkFrvO_M"
    )

# The Big Shot movie: movie title, storyline, poster image and movie trailer
the_big_shot = media.Movie(
    "The Big Short (2015)",
    "Four denizens in the world of high-finance predict the credit and housing"
    "bubble collapse of the mid-2000s.",
    "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=O1X0KDdS5Bw"
    )

# Sully movie: movie title, storyline, poster image and movie trailer
sully = media.Movie(
    "Sully (2016)",
    "The story of Chesley Sullenberger, an American pilot who became a hero"
    "after landing his damaged plane.",
    "https://upload.wikimedia.org/wikipedia/en/8/82/Sully_xxlg.jpeg",  # NOQA
    "https://www.youtube.com/watch?v=mjKEXxO2KNE"
    )

# La La Land movie: movie title, storyline, poster image and movie trailer
la_la_land = media.Movie(
    "La La Land (2016)",
    "While waiting for their big breaks, two proper L.A. dreamers, attempt to"
    "reconcile relationship.",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # NOQA
    "https://www.youtube.com/watch?v=je0aAf2f8XQ"
    )

# Generate a list of Movie instances
movies = [
    memento,
    the_dark_knight,
    black_swan,
    the_imitation_game,
    ex_machina,
    kingsman,
    the_big_shot,
    sully, la_la_land
    ]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
