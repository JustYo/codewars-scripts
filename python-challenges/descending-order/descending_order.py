def store_the_doublons(num_list: list):
    doublon_dict = {}
    for num_item in num_list:
        if num_list.count(num_item) > 1:
            doublon_dict.update({int(num_item):num_list.count(num_item)})

    return doublon_dict

def test_numbers(num_list):
    bool_list = []
    for num_item in num_list:
        bool_list2 = []
        for num_item2 in num_list:
            if num_item2 > num_item:
                bool_list2.append(True)
            elif num_item2 < num_item:
                bool_list2.append(False)
        bool_list.append(bool_list2)
    return bool_list

def descending_order(num):
    # Bust a move right here
    s = 0
    if num > 0:
        num_str = str(num)
        num_list = list(num_str)

        doublon_dict = store_the_doublons(num_list)
        bool_list = test_numbers(num_list)
        num_list_buffer = [0] * len(num_list)

        for index, boolbool in enumerate(bool_list):
            count_true = boolbool.count(True)
            num_item = int(num_list[index])
            if num_item in doublon_dict.keys():
                for index2 in range(doublon_dict[num_item]):
                    num_list_buffer[count_true + index2] = num_item
            else:
                num_list_buffer[count_true] = num_item

        s = map(str, num_list_buffer)  # ['1','2','3']
        s = "".join(s)  # '123'
        s = int(s)
    return s