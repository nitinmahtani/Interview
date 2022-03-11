import math



def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2
    count = 0
    i = 0
    while i < len(array):
        if array[i] == 0:
            count += 1
            array.pop(i)
            i -= 1
        i += 1
    for i in range(count):
        center = math.floor(len(array)/2)
        if len(array) % 2 == 0 or len(array) == 1:
            array.insert(center, 0)
        else:
            array.insert(center + 1, 0)
    return array


if __name__ == "__main__":
    # write your debug code here
    pass
