"""
Movie Recommendation System

A command-line Python application that recommends movies
based on user preferences using a simple scoring algorithm.
"""

from random import shuffle

movies = [
    {"title":"Inception","genre":"sci fi","mood":"mind bending","complexity":"complex","language":"b2","platform":"netflix","duration":2.5},

    {"title":"Interstellar","genre":"sci fi","mood":"thoughtful","complexity":"complex","language":"b2","platform":"amazon prime","duration":2.8},

    {"title":"The Prestige","genre":"mystery","mood":"mind bending","complexity":"complex","language":"b2","platform":"amazon prime","duration":2.2},

    {"title":"The Dark Knight","genre":"crime","mood":"dark","complexity":"medium","language":"b2","platform":"netflix","duration":2.5},

    {"title":"Shutter Island","genre":"mystery","mood":"dark","complexity":"complex","language":"b2","platform":"netflix","duration":2.3},

    {"title":"Prisoners","genre":"crime","mood":"intense","complexity":"medium","language":"b2","platform":"amazon prime","duration":2.5},

    {"title":"Se7en","genre":"crime","mood":"dark","complexity":"medium","language":"b2","platform":"netflix","duration":2.1},

    {"title":"Fight Club","genre":"drama","mood":"mind bending","complexity":"complex","language":"b2","platform":"amazon prime","duration":2.3},

    {"title":"The Matrix","genre":"sci fi","mood":"mind bending","complexity":"medium","language":"b2","platform":"netflix","duration":2.3},

    {"title":"Edge of Tomorrow","genre":"action","mood":"exciting","complexity":"easy","language":"b1","platform":"amazon prime","duration":1.9},

    {"title":"John Wick","genre":"action","mood":"intense","complexity":"easy","language":"b1","platform":"netflix","duration":1.7},

    {"title":"Mad Max: Fury Road","genre":"action","mood":"exciting","complexity":"easy","language":"b1","platform":"amazon prime","duration":2.0},

    {"title":"Top Gun: Maverick","genre":"action","mood":"inspiring","complexity":"easy","language":"b1","platform":"amazon prime","duration":2.2},

    {"title":"Mission: Impossible - Fallout","genre":"action","mood":"exciting","complexity":"medium","language":"b2","platform":"netflix","duration":2.5},

    {"title":"The Bourne Identity","genre":"action","mood":"intense","complexity":"medium","language":"b2","platform":"amazon prime","duration":2.0},

    {"title":"Knives Out","genre":"mystery","mood":"fun","complexity":"medium","language":"b2","platform":"netflix","duration":2.2},

    {"title":"Glass Onion","genre":"mystery","mood":"fun","complexity":"easy","language":"b2","platform":"netflix","duration":2.3},

    {"title":"Gone Girl","genre":"thriller","mood":"dark","complexity":"complex","language":"c1","platform":"amazon prime","duration":2.5},

    {"title":"The Silence of the Lambs","genre":"thriller","mood":"dark","complexity":"medium","language":"c1","platform":"amazon prime","duration":2.0},

    {"title":"Nightcrawler","genre":"crime","mood":"dark","complexity":"medium","language":"c1","platform":"netflix","duration":2.0},

    {"title":"The Social Network","genre":"drama","mood":"thoughtful","complexity":"medium","language":"c1","platform":"amazon prime","duration":2.0},

    {"title":"Whiplash","genre":"drama","mood":"intense","complexity":"medium","language":"b2","platform":"amazon prime","duration":1.8},

    {"title":"The Pursuit of Happyness","genre":"drama","mood":"inspiring","complexity":"easy","language":"b1","platform":"netflix","duration":2.0},

    {"title":"Forrest Gump","genre":"drama","mood":"inspiring","complexity":"easy","language":"b1","platform":"amazon prime","duration":2.3},

    {"title":"The Shawshank Redemption","genre":"drama","mood":"inspiring","complexity":"medium","language":"b2","platform":"amazon prime","duration":2.4},

    {"title":"The Green Mile","genre":"drama","mood":"emotional","complexity":"medium","language":"b2","platform":"amazon prime","duration":3.1},

    {"title":"A Beautiful Mind","genre":"drama","mood":"thoughtful","complexity":"medium","language":"b2","platform":"amazon prime","duration":2.3},

    {"title":"Arrival","genre":"sci fi","mood":"thoughtful","complexity":"complex","language":"c1","platform":"netflix","duration":2.0},

    {"title":"The Martian","genre":"sci fi","mood":"inspiring","complexity":"easy","language":"b1","platform":"hotstar","duration":2.4},

    {"title":"The Imitation Game","genre":"drama","mood":"thoughtful","complexity":"medium","language":"b2","platform":"netflix","duration":1.9},

    {"title":"Ford v Ferrari","genre":"sport","mood":"exciting","complexity":"easy","language":"b1","platform":"hotstar","duration":2.5},

    {"title":"Rush","genre":"sport","mood":"intense","complexity":"easy","language":"b1","platform":"amazon prime","duration":2.0},

    {"title":"Moneyball","genre":"sport","mood":"thoughtful","complexity":"medium","language":"b2","platform":"netflix","duration":2.2},

    {"title":"Coach Carter","genre":"sport","mood":"inspiring","complexity":"easy","language":"b1","platform":"netflix","duration":2.3},

    {"title":"The Conjuring","genre":"horror","mood":"intense","complexity":"easy","language":"b1","platform":"amazon prime","duration":1.9},

    {"title":"A Quiet Place","genre":"horror","mood":"intense","complexity":"easy","language":"b1","platform":"netflix","duration":1.5},

    {"title":"Get Out","genre":"horror","mood":"thoughtful","complexity":"medium","language":"b2","platform":"amazon prime","duration":1.7},

    {"title":"Free Guy","genre":"comedy","mood":"fun","complexity":"easy","language":"b1","platform":"hotstar","duration":1.9},

    {"title":"The Nice Guys","genre":"comedy","mood":"fun","complexity":"easy","language":"b2","platform":"netflix","duration":1.9},

    {"title":"The Grand Budapest Hotel","genre":"comedy","mood":"fun","complexity":"medium","language":"c1","platform":"amazon prime","duration":1.7}
]

shuffle(movies)





def inputs():
    """Collect and validate user preferences."""

    genre_choices = ("action", "thriller", "mystery", "crime", "sci fi", "drama", "comedy", "adventure", "horror", "sport", "any")

    mood_choices = ("intense", "fun", "dark", "emotional", "thoughtful", "exciting", "inspiring", "mind bending", "any")

    complexity_choices = ("easy", "medium", "complex", "any")

    lang_difficulty_choices = ("b1", "b2", "c1", "any")

    platform_choices = ("netflix", "amazon prime", "hotstar", "any")

    print("Enter Your Preferences ->\n")


    while True:
        genre = input(f"Choose a genre - {', '.join(genre_choices)}: ").strip().lower()

        if genre in genre_choices:
            break
        else:
            print("Choose a valid genre.")

    while True:
        mood = input(f"Choose a mood - {', '.join(mood_choices)}: ").strip().lower()

        if mood in mood_choices:
            break
        else:
            print("Choose a valid mood.")

    while True:
        complexity = input(f"Choose complexity - {', '.join(complexity_choices)}: ").strip().lower()

        if complexity in complexity_choices:
            break
        else:
            print("Choose a valid complexity.")

    while True:
        lang_diff = input(f"Choose English difficulty - {', '.join(lang_difficulty_choices)}: ").strip().lower()

        if lang_diff in lang_difficulty_choices:
            break
        else:
            print("Choose a valid difficulty.")

    while True:
        platform = input(f"Choose a platform - {', '.join(platform_choices)}: ").strip().lower()

        if platform in platform_choices:
            break
        else:
            print("Choose a valid platform.")

    while True:
        try:
            # for 30 minute buffer
            avail_time = float(input("How much time do you have (in hours)? ")) + 0.5

            if avail_time <= 0:
                print(f"You entered {avail_time}, which is invalid.")
            else:
                break

        except ValueError:
            print("You entered an incorrect value.")

    return genre, mood, complexity, lang_diff, platform, avail_time





def calculate_scores(movies, genre, mood, complexity, language, platform, duration):
    """Calculate a matching score for each movie."""

    scored_movies = []

    for movie in movies:
        score = 0
        if movie["genre"] == genre or "any" == genre:
            score += 1

        if movie["mood"] == mood or "any" == mood:
            score += 1

        if movie["complexity"] == complexity or "any" == complexity:
            score += 1

        if movie["language"] == language or "any" == language:
            score += 1

        if movie["platform"] == platform or "any" == platform:
            score += 1

        if movie["duration"] <= duration:
            score += 1

        movie_copy = movie.copy()
        movie_copy["score"] = score
        scored_movies.append(movie_copy)

    return scored_movies
    




def sort_movies(scored_movies):
    """Sort movies by score in descending order."""

    sorted_movies = sorted(
        scored_movies,
        key=lambda movie: movie["score"],
        reverse=True
    )

    return sorted_movies





def display(sorted_movies):
    """Display the top movie recommendations."""

    TOTAL_SCORE = 6
    MIN_SCORE = 4

    found = False

    for count, movie in enumerate(sorted_movies[:3], start=1):

        if movie["score"] >= MIN_SCORE:

            found = True

            match_percent = int((movie["score"] / TOTAL_SCORE) * 100)

            print("--------------------------")
            print(f"{count}. {movie['title']}")
            print(f"Genre: {movie['genre'].title()}")
            print(f"Platform: {movie['platform'].title()}")
            print(f"Duration: {movie['duration']} hrs")
            print(f"Match: {match_percent}%")
            print("--------------------------\n")

    if not found:
        print("Sorry, no good matches found.")
        print('Try selecting "Any" for one or more preferences.')





"""Final Execution"""

if __name__ == "__main__":

    genre, mood, complexity, lang_diff, platform, avail_time = inputs()

    scored_movies = calculate_scores(
        movies, 
        genre, 
        mood, 
        complexity, 
        lang_diff, 
        platform, 
        avail_time
        )

    sorted_movies = sort_movies(scored_movies)

    display(sorted_movies)


