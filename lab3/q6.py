#Write a python function ‘parse_csv’ to parse csv 
#(comma separated values) files.
import csv

def parse(file):
    with open(file, 'r') as f:
        data = csv.reader(f)
        for row in data:
            print(row)

parse('data.csv')