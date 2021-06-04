#Generalize the above implementation of csv parser to support any delimiter and comments.

import csv

def parse(file, delimiter):
    with open(file, 'r') as f:
        data = csv.reader(f, delimiter = delimiter)
        for row in data:
            print(row)

parse('data.csv', ',')