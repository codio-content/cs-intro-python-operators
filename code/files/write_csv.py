import csv
import os

path = "student_folder/csv"
with open(os.path.join(path,"write_practice.csv"), "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerows([
      ["Artist", "Album", "Copies"],
      ["Michael Jackson", "Thriller", "47 million"],
      ["Eagles", "Their Greatest Hits 1971-1975", "38 million"],
      ["Eagles", "Hotel California", "26 million"]
    ])