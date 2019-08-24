# Function to find winner of an election where votes 
# are represented as candidate names 
from collections import Counter
from collections import defaultdict


def winner(ballot):
    votes = Counter(ballot)
    votes_candidates = defaultdict(list)
    for (key, value) in votes.items():
        votes_candidates[value].append(key)

    max_vote = sorted(votes_candidates.keys())[-1]
    candidates = sorted(votes_candidates[max_vote])
    return candidates[-1]


if __name__ == "__main__":
    input = ["Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary", ]
    winner(input)
