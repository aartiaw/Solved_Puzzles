"""Maximum sum increasing subsequence:
   subsequence - 'xoriantsystems' -- 'xoatysts' is a subsequence of the
   parent string (need not to be contiguous). Return the sum of the maximum
   sum increasing subsequence such that the integers in the subsequence are
   sorted in non-decreasing order.
   input: length of the array, array elements
   Input:  [1, 104, 2, 3, 100, 4, 6]
   --> [1, 2, 3 ,100]
   Output: 106

   Input:  [3, 2, 6, 4, 5, 1]
   --->[3, 4, 5]
   output : 12
"""

def max_sum_subseq(arr):
    """Function to calculate maximum sum increasing subsequence."""

    """List to store subsequence"""
    ans_subseq = []
    """List to store sum till a particular element of actual array"""
    copy_arr = list(arr)
    """List to store position element giving max sum"""
    actual_seq = [i for i in range(len(arr))]

    """Calculate maximum sum."""
    for i in range(1, len(arr)):
        for j in range(0, i):
            """Calculate sum only if it is increasing subsequence and sum is
               greater than previous sum. Also store position of such element
               in actual_seq list.
            """
            if arr[j] < arr[i] and copy_arr[i] < (copy_arr[j] + arr[i]):
                copy_arr[i] = copy_arr[j] + arr[i]
                actual_seq[i] = j
    max_sum = max(copy_arr)

    """Calculate maximum sum giving subsequence."""
    position = copy_arr.index(max(copy_arr))
    while True:
        ans_subseq.insert(0, arr[position])
        """Break the loop when subsequence is found."""
        if sum(ans_subseq) == max(copy_arr):
            break
        position = actual_seq[position]

    print "Maximum sum = ", max_sum, "\nCorresponding increasing subsequence = ", ans_subseq

if __name__ == "__main__":
    arr = [1, 104, 2, 3, 100, 4, 6]
    max_sum_subseq(arr)


