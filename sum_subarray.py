"""Given an array of integers, find the maximum sum
   of a contiguous subarray(not subsequence)
   input : [-2, -3, 4, -1, -2, 1, 5, -3]
   --> 4 + (-1) + (-2) + 1 + 5
   output : 7
"""

def get_max_sum(arr):
    """Function to get maximum sum from subarray."""
    if arr:
        s = arr[0]
        max_sum = arr[0]
        for i in range(1, len(arr)):
            s = max(arr[i], s+arr[i])
            max_sum = max(max_sum, s)
        return max_sum

    else:
        return 0


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    max_sum = get_max_sum(arr)
    print "Maximum sum of subarray: ", max_sum

