import csv, os

file_name = "mlb_data.csv"
file_path = "student_folder/.exercises"

def best_team(f_name, f_path):
    """Read a CSV of baseball data.
    Return the team name with the most wins"""
    with open(os.path.join(f_path, f_name), "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        most_wins = 0
        best_team = ""
        for row in reader:
            if int(row[3]) > most_wins:
                most_wins = int(row[3])
                best_team = row[0]
        return best_team
      
print(best_team(file_name, file_path))