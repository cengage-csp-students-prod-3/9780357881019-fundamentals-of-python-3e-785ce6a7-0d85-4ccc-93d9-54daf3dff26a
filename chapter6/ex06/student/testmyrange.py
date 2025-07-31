def myRange(start, stop=None, step=None):
    # Normalize parameters
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = 1

    # Guard clause: step cannot be zero
    if step == 0:
        return []

    # Determine direction validity
    if (start < stop and step < 0) or (start > stop and step > 0):
        return []

    # Generate the list manually
    result = []
    i = start
    if step > 0:
        while i < stop:
            result.append(i)
            i += step
    else:
        while i > stop:
            result.append(i)
            i += step  # step is negative

    return result


# Test cases to verify the implementation
def main():
    print(myRange(10))           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(myRange(1, 10))        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(myRange(1, 10, 2))     # [1, 3, 5, 7, 9]
    print(myRange(10, 1, -1))    # [10, 9, 8, 7, 6, 5, 4, 3, 2]
    print(myRange(10, 1, 1))     # []
    print(myRange(1, 10, -1))    # []
    print(myRange(1, 10, 0))     # []


if __name__ == "__main__":
    main()
