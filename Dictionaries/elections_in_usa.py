''' As you know, the president of USA is elected not by direct vote, but through a two-step voting. 
    First elections are held in each state and determine the winner of elections in that state. 
    Thereafter, the state election is going: in this election, every state has a 
    certain the number of votes — the number of electors from that state. In practice, 
    all the electors from the state of voted in accordance with the results of the vote within a state.
    The first line contains the number of records. After that, each entry contains the name of 
    the candidate and the number of votes they got in one of the states. 
    Count the total results of the elections: sum the number of votes for each candidate. 
    Print candidates in the alphabetical order. '''



# Read the number of records
n = int(input())
# Initialize an empty dictionary to store the votes for each candidate
election_results = {}

# Read each record and update the vote count for each candidate
for _ in range(n):
    candidate, votes = input().split()
    votes = int(votes)
    if candidate in election_results:
        election_results[candidate] += votes
    else:
        election_results[candidate] = votes

# Print the candidates and their total vote count in alphabetical order
for candidate in sorted(election_results.keys()):
    print(candidate, election_results[candidate])
