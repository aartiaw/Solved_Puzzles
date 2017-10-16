"""Given a value N, if we want to make change for N rupees, and we have
   infinite supply of each of S = [S1, S2, .. , Sm] valued coins,
   how many ways can we make the change? The order of coins doesn't matter.
   e.g. For N = 10 and S = {2, 5, 3, 6},
        there are 5 solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5}, {5,5}
        So the output should be 5.
"""

def coin_change(total, coins_arr):
    """Function to calculate combination of coins that give sum = total"""

    """Initialize a list whose index corresponds to sum and
       value at that index will correspond to number of ways
       that sum can be obtained.
    """
    combinations = [0 for x in range(total+1)]

    """Zeroth position = 1, since there is only 1 way to get sum 0
       by not selecting any of the coins.
    """
    combinations[0] = 1

    """Find number of ways that give sum value corresponding to
       index of combinations list by iterating over all coins."""
    for coin in coins_arr:
        for i in range(len(combinations)):
            if(i >= coin):
                combinations[i] += combinations[i-coin]
   
    print "Total combinations: ", combinations[total]


if __name__ == "__main__":
    coins_arr = map(lambda x: int(x), raw_input("Enter array of coins: \n").split(" "))
    total = int(raw_input("Enter total: "))
   
    coin_change(total, coins_arr)

