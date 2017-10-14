"""Given an array and a k, find out if a pair of elements
   exists with sum as k. Give two solutions one for sorted array
   and one for unsorted array.
"""

def unsorted_array(arr, k):
    """Logic to find pair that gives sum=k for unsorted array."""
    for i in range(len(arr)):
        pair_num = k - arr[i]
        j = i + 1
        for j in range(len(arr)):
            if arr[j] == pair_num:
                return 1
    return 0

def sorted_array(arr, k):
    """Logic to find pair that gives sum=k for sorted array."""
    for i in range(len(arr)):
        if arr[i] > k:
            continue
        pair_num = k - arr[i]
        j = i + 1
        for j in range(len(arr)):
            if arr[j] == pair_num:
                return 1
    return 0


if __name__ == "__main__":
    arr = map(lambda x: int(x), raw_input("Enter array of numbers: \n").split())
    k = int(raw_input("Enter a value (sum): "))

    """For unsorted array"""
    check1 = unsorted_array(arr, k)
    if check1 == 1:
        print "Pair of elements with this sum exists!"
    else:
        print "Pair of elements with this sum does'nt exists!"

    """For sorted array"""
    desc_arr = sorted(arr, reverse=True)
    check2 = sorted_array(desc_arr, k)
    if check2 == 1:
        print "Pair of elements with this sum exists!"
    else:
        print "Pair of elements with this sum does'nt exists!"

