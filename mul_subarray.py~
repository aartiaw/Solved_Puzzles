"""Max product subarray same as the Max sum subarray."""

def get_max_product(arr):
    """Function to get maximum sum from subarray."""
    if arr:
        p = arr[0]
        max_product = arr[0]
        for i in range(1, len(arr)):
            p = max(arr[i], p*arr[i])
            max_product = max(max_product, p)
        return max_product

    else:
        return 0


if __name__ == "__main__":
    arr = [6, -3, -10, 0, 2]
    max_product = get_max_product(arr)
    print "Maximum product of subarray: ", max_product

