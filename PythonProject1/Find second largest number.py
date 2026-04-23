def sec_largest(lst):
    global largest, sec
    if len(lst) < 2:
        print("can't find sec. largest")

    elif lst[0] > lst[1]:
        largest = lst[0]
        sec = lst[1]

    else:
        largest = lst[1]
        sec = lst[0]

    for i in range(2,len(lst)):
        if lst[i]>largest:
            sec = largest
            largest = lst[i]
        elif lst[i]>sec and lst[i]<largest and lst[i]!=largest:
            sec = lst[i]
    return sec

list = [2,4,6,8,10]
print(sec_largest(list))

