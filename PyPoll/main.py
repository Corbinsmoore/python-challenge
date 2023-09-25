import os 
import csv

#importing csv
csvpath = os.path.join('Resources', 'election_data.csv')

#open csv
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#defining variables

    total_votes = 0
    percent_of_votes = 0
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0
    winner = 0

#loop 
    for row in csvreader:
        total_votes +=1
        if row[2] == "Charles Casper Stockham":
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes  +=1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes  +=1

# make dctionaries 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [stockham_votes, degette_votes, doane_votes]

#zipping candidates and votes
votes_dict = dict(zip(candidates, candidate_votes))
print(votes_dict)
winner = max(votes_dict, key=votes_dict.get)

#calculate percent of vote per candidate 
percent_stockham = (stockham_votes/total_votes) * 100
percent_degette = (degette_votes/total_votes) * 100
percent_doane = (doane_votes/total_votes) * 100

#analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes : {total_votes}" )
print("-------------------------")
#print percent of votes for each candidate and total votes
print(f"Charles Casper Stockham: {percent_stockham:.3f}% ({stockham_votes})")
print(f"Diana Degette: {percent_degette:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {percent_doane:.3f}% ({doane_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export results 
analysis = os.path.join("Analysis", "Election_analysis.txt")
with open(analysis, "w") as file:

   file.write("Election Results")
   file.write("\n")
   file.write("-------------------------")
   file.write("\n")
   file.write(f"Total Votes : {total_votes}" )
   file.write("\n")
   file.write("-------------------------")
   file.write("\n")
   file.write(f"Charles Casper Stockham: {percent_stockham:.3f}% ({stockham_votes})")
   file.write("\n")
   file.write(f"Diana Degette: {percent_degette:.3f}% ({degette_votes})")
   file.write("\n")
   file.write(f"Raymon Anthony Doane: {percent_doane:.3f}% ({doane_votes})")
   file.write("\n")
   file.write("-------------------------")
   file.write("\n")
   file.write(f"Winner: {winner}")
   file.write("\n")
   file.write("-------------------------")
 