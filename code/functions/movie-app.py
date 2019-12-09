import os, csv, operator

path = "student_folder/.labs"
file_name = "movie_data.csv"

def fetch_movie_data(path, file_name):
    """Return movie data from a CSV file"""
    with open(os.path.join(path, file_name), "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

def print_movie_data(data):
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data:
      print("{:36} {:10} {:18} {:16} {}".format(title, genre, rotten, gross, year))
      
def sort_movie_data(data, index, descending):
    """Sort movie data based on the column data"""
    header = data[0]
    sorted_movies = data[1:]
    sorted_movies.sort(key=operator.itemgetter(index))
    if descending:
        sorted_movies.reverse()
    sorted_movies.insert(0, header)
    return sorted_movies
      
movie_data = fetch_movie_data(path, file_name) 
print_movie_data(sort_movie_data(movie_data, 0, True))