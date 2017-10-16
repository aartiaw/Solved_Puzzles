"""The stock prices of one unit of a stock is given.
   You can buy and sell only once.
   Find out the maximum profit you can make.
   input : 100 20 30 110 10 60 200 10
   output : 200-20 = 180
"""

def get_max_profit(arr):
    """Function to calculate maximum profit using dynamic programming."""
    max_profit = 0
    profit = 0

    for i in range(len(arr)):
        sub_arr = [arr[num] for num in range(i+1)]

        if sub_arr:
            profit = arr[i] - min(sub_arr)
            if max_profit < profit:
                max_profit = profit
    print "Maximum profit = ", max_profit
    

if __name__ == "__main__":
    arr = map(lambda x: int(x), raw_input("Enter stock prices: \n").split(" "))
    get_max_profit(arr)
