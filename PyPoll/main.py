import pandas as pd
#read csv
data = pd.read_csv('PyPoll/Resources/election_data.csv')
#calculate total votes
tot_votes = len(data)
#create variables for ending winner
winner = ""
win_vote = 0

print(f"""
Election Results
-------------------------
Total Votes: {tot_votes}
-------------------------""")
#for loop using groupby to most easily get the candidate and the number of rows(votes)
for c, rows in data.groupby(["Candidate"]):
    pct_votes = round(100*len(rows)/tot_votes,3)
    can_votes = len(rows)
#if statement to calculate the winner in the for loop
    if can_votes > win_vote:
        winner = c
        win_vote = can_votes
    
    print(f"{c}: {pct_votes}% ({can_votes})")

print(f"""-------------------------
Winner: {winner}
-------------------------
""")