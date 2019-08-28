# When John gambles at the casino, he always uses a special system of tactics that he devised himself. It's based on always betting in one of two ways in each game:
# betting exactly one chip (to test his luck)
# betting all-in (he bets everything he has).
# Wins in the casino are paid equal to the wager, so if he bets C chips and wins, he gets 2C chips back. If he loses, he doesn't get any chips back.

# It was a very lucky day yesterday and John won every game he played, starting with one chip and leaving the casino with N chips. We also know that John played all-in no more than K times. Your task is to calculate the smallest possible number of rounds he could have played.

# Note: betting just one chip is never considered playing all-in.

# that, given an integer N and an integer K, returns the minimum number of rounds that are necessary for John to leave the casino with N chips, having played all-in no more than K times.

# Given N = 8 and K = 0, the answer is 7. K is 0 so John bets 1 chip in each round. The number of chips were as follows:

#   at the beginning: 1
#
#   after the 1st round: 2 (he bet 1)
#   after the 2nd round: 3 (he bet 1)
#   after the 3rd round: 4 (he bet 1)
#   after the 4th round: 5 (he bet 1)
#   after the 5th round: 6 (he bet 1)
#   after the 6th round: 7 (he bet 1)
#   after the 7th round: 8 (he bet 1)
#
#   he played all-in 0 times

# Given N = 10 and K = 10, the answer is 4. The shortest game would be:

#   at the beginning: 1
#
#   after the 1st round: 2 (he bet 1)
#   after the 2nd round: 4 (all-in)
#   after the 3rd round: 5 (he bet 1)
#   after the 4th round: 10 (all-in)
#
#   he played all-in 2 times

#  algorithm for the following assumptions:
# N is an integer within the range [1..2,147,483,647]
# K is an integer within the range [1..100]
def solution(N, K):
    rounds = 0
    while K > 0 and N > 0:
        if N % 2 == 0:
            N //= 2
            K -= 1
            rounds += 1
        elif N % 2 == 1:
            N -= 1
            rounds += 1

    # if there are no all-in-one left, then there will be total N-1 steps
    rounds = rounds + N - 1
    return rounds


res = solution(18, 2)
print(res)
res = solution(100, 2)
print(res)
res = solution(10, 10)
print(res)
res = solution(1000000000, 100)
print(res)
