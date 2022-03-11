def select_max(array):
    if not array:
        return None
    maxi = array[0]
    for item in array:
        if item > maxi:
            maxi = item
    return maxi


if __name__ == "__main__":
    # write your debug code here
    pass
