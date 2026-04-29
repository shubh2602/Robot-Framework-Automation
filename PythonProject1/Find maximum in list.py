def max_num(list):

    max = list[0]
    for num in list:
        if num > max:
            max = num

    return max

list1 = [2,10,3,7]
print(max_num(list1))