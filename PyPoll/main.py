import os
import csv

def read_file(path):
    with open(path) as f:
        csvreader = csv.reader(f, delimiter = ',')
        header = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
    return data

def vote_count(data):    
    candidates = {}
    total_votes = 0
    for row in data:
        candidate = row[2]
        total_votes += 1
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    return [candidates, total_votes]

def calculate_results(candidates, total_votes):
    winning_votes = 0
    winner = ""
    for candidate, votes in candidates.items():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes
    print_winner = f"The winner is {winner} with {winning_votes} votes!"
    print_candidates = ""
    for candidate, votes in candidates.items():
        print_candidates = print_candidates + f"{candidate}: {votes} votes ({int(round((votes/total_votes)*100, 2))}%)\n"
    
    
    results = f"{print_winner}\n--------------------------------------------\n{print_candidates}"
    return results

vote_csv = read_file("election_data.csv")
candidates, total_votes = vote_count(vote_csv)
results = calculate_results(candidates, total_votes)
print(results)