# Movie DB Dictionary Project

# Add a movie
movie_db = {}

# Add a movie
def add_movie():
    # Got data from user and saved into variables
    title = input('Enter the movie title:  ')
    year = input('Enter the movie year:  ')
    genre = input('Enter the movie genre:  ')
    director = input('Enter the movie director:  ')
    actors = input('Enter the name of actors(comma separated):  ')

     # Used data to create a movie in the database
    movie_db[title] = { 
        'year' :  year,
        'genre' : genre,
        'director':  director,
        'actors':  actors.split(",")
    }

    print(f'Success:  {title} added!' )

# Edit a movie

# Delete a movie

# View all movies
def show_all():
    print('All movies in Database') 
    print('==============')
    for movie in movie_db:
        print(f"Movie:  {movie}")
        for key, value in movie_db[movie].items():
            print(f"{key}:  {value}")
        print('==============')

# Search Movies

# Save and load movie from a file

# Error handling

# Data validation

# We have to find a way, to repeatly ask the user what action they want to take
while True:
    print('==== Movie Database MGMT System ====')
    print('1. Exit')
    print('2. Add Movie')
    print('3. Show All Movies')

    choice = input('What do you want to do?')

    if choice == '1':
        print('Goodbye.  Comback soon!')
        break
    elif choice == '2':
        add_movie()
    elif choice == '3':
        show_all()
    else:
        print('Invalid Option, Please try again.')