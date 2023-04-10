from math import sqrt

def find_next_square(sq):
    result = 0
    if sq % sqrt(sq) != 0.0:
        result = -1
    elif sq == 0:
        result = -1
    else:
        sq = sq + 1
        while sq % sqrt(sq) != 0.0:
            sq = sq + 1
        result = sq
    return result


print(find_next_square(121))
