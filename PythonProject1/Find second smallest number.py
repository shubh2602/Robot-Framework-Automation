def sec_largest(lst):
    if len(lst) < 2:
        print("can't find sec. smallest")

    elif lst[0] < lst[1]:
        smallest = lst[0]
        sec_smallest = lst[1]

    else:
        smallest = lst[1]
        sec_smallest = lst[0]

    for i in range(2,len(lst)):
        if lst[i]<smallest:
            sec_smallest = smallest
            smallest = lst[i]
        elif lst[i]<sec_smallest and lst[i]>smallest:
            sec_smallest = lst[i]
    return sec_smallest

list = [2,4,3,8,10]
print(sec_largest(list))

