def small_num(list):

    small = list[0]
    for num in list:
        if num < small:
            small = num

    return small

list1 = [2,10,3,7,1]
print(small_num(list1))