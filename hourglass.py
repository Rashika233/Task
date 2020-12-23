def hourglass_sums(arr):
    """Generate all sums of hourglasses in the array."""
    num_rows = len(arr)
    num_cols = len(arr[0])
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            yield (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                   arr[i + 1][j + 1] +
                   arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

arr([1 1 1 0 0 0],
[0 1 0 0 0 0],
[1 1 1 0 0 0].
[0 0 2 4 4 0],
[0 0 0 2 0 0
0 0 1 2 4 0)
def max_hourglass_sum(arr):
    """Maximal hour glass sum in the array."""
    return max(hourglass_sums(arr))