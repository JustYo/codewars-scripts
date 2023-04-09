def array_diff(a, b):
    # subtract one list from another and returns the result.
    a_modify = []
    for a_item in a:
        if a_item not in b:
            a_modify.append(a_item)
    return a_modify
