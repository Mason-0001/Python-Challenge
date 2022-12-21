import pandas as pd

data = pd.read_csv('PyPoll/Resources/election_data.csv')
tot_votes = len(data)
winner = ""
win_vote = 0
print(f"""
Election Results
-------------------------
Total Votes: {tot_votes}
-------------------------""")

for c, rows in data.groupby(["Candidate"]):
    pct_votes = round(100*len(rows)/tot_votes,3)
    can_votes = len(rows)
    if can_votes > win_vote:
        winner = c
        win_vote = can_votes
    
    print(f"{c}: {pct_votes}% ({can_votes})")

print(f"""-------------------------
Winner: {winner}
-------------------------
""")