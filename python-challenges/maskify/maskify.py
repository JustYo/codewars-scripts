def maskify(code):
    list_code = list(code)
    last_four_digits = list_code[-4:]
    final_list = []
    for i in range(len(list_code) - 4):
        final_list.append("#")
    final_list.append(''.join(last_four_digits))
    return ''.join(final_list)

print(maskify("iyvubyhojnok,l"))