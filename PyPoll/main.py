import os 
import csv

#importing csv
csvpath = os.path.join(".", "Resources", "election_data.csv")

#open csv
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter="")
