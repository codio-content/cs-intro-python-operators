with open("read_practice.txt", "r") as source, open("destination.txt", "w") as dest:
    for line in source.readlines():
        line += "\n"
        dest.write(line)