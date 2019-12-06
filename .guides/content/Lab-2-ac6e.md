## Lab 2 - Building a Command Line Application

The next couple of labs will walk you through making a command line application that sorts a slightly modified version of this [movie data](https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea). 

<details><summary>**How has the CSV file been modified?**</summary>The CSV file used for this project only contains the columns for the film, genre, Rotten Tomatoes score, the worldwide gross, and the year the film was released. Including all of the data would be too world for the terminal. Rows of data would go onto a second line, which hurt human readability. In addition, duplicates were removed, and a few of the genres needed to be capitalized.</details>

This lab focuses on reading the information from a CSV file, and then printing the information in a human readable way.

### Reading the CSV
The most important function is the one that reads the information from a CSV file. Once the file has been read, the information will be stored in the variable `movie_data`, and the file will be closed. There is no need to leave the file open for this program. You will need global variables for the path and file name of the CSV file. The program should print `None`.

```python
import os, csv

path = "student_folder/.labs"
file_name = "movie_data.csv"

def fetch_movie_data(path, file_name):
    """Return movie data from a CSV file"""
    pass

movie_data = fetch_movie_data(path, file_name) 
print(movie_data)
```

{try it}(python3 code/functions/movie-app.py 1)

<details><summary>**What does "pass" mean?**</summary>Think of `pass` as a placeholder for a function. We know that the function needs to do something or else an error message will appear. Using `pass` means that the function will not do anything, but there will not be an error message either.</details>

Using `with open`, read the entire CSV file and then pass it to a `csv.reader`. Create the local variable `movie_info` and set it to an empty list. Use a for loop to iterate through the file and append each row to the list `movie_info`. Once done iterating through the file, return `movie_info`. Running the program now should return a list of lists with a bunch of information that is hard to understand.

```python
import os, csv

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

movie_data = fetch_movie_data(path, file_name) 
print(movie_data)
```

{try it}(python3 code/functions/movie-app.py 2)

### Printing the Movie Information
Since this is a command line application, the output should be easy to read for humans. The `print` command will print square brackets, and it does not format the output. It is not sufficient. Create the function `print_movie_data` that takes the parameter `data`. Use the unpacking method to be able to reference each element of the list. The `{:10}` syntax adds padding to the right of the string. This will align all of the data in neat rows. Add a function call for `print_movie_data` and remove `print(movie_data)`.

<details><summary>**Formatting a String with Padding**</summary><img src=".guides/images/formatting-columns.png" /></details>

```python
import os, csv

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
      
movie_data = fetch_movie_data(path, file_name) 
print_movie_data(movie_data)
```

{try it}(python3 code/functions/movie-app.py 3)

{Check It!|assessment}(fill-in-the-blanks-932559392)
