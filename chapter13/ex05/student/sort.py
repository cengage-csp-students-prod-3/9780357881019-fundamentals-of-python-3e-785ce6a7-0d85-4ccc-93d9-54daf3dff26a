def selectionSort(lst, reverse=False):
    n = len(lst)
    for i in range(n - 1):
        # Assume the current position holds the min (or max if reverse=True)
        idx_extreme = i
        for j in range(i + 1, n):
            if (not reverse and lst[j] < lst[idx_extreme]) or (reverse and lst[j] > lst[idx_extreme]):
                idx_extreme = j
        # Swap if a new min/max found
        if idx_extreme != i:
            lst[i], lst[idx_extreme] = lst[idx_extreme], lst[i]

def main():
    """Tests with four lists."""
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst)
    print(lyst)
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst, reverse = True)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst, reverse = True)
    print(lyst)

if __name__ == "__main__":
    main()