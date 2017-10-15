"""Max product subarray same as the Max sum subarray."""

def get_max_product(arr):
    """Function to get maximum product from subarray."""
    if arr:
        ans = arr[0]
        cur_max_product = arr[0]
        prev_max_product = arr[0]
        prev_min_product = arr[0]
        for i in range(1, len(arr)):
            cur_max_product = max(arr[i], prev_max_product*arr[i],
                                  prev_min_product*arr[i])
            cur_min_product = min(arr[i], prev_max_product*arr[i],
                                  prev_min_product*arr[i])
            ans = max(ans, cur_max_product)

            prev_max_product = cur_max_product
            prev_min_product = cur_min_product
        return ans

    else:
        return 0


if __name__ == "__main__":
    arr = [6, -3, -10, 0, 2]
    max_product = get_max_product(arr)
    print "Maximum product of subarray: ", max_product

