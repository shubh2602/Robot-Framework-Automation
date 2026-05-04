def Rotate_list_right_by_one_position(l1):

    if len(l1) == 0:
        return l1

    last_ele = l1[-1]

    for i in range(len(l1)-1, 0, -1):
        l1[i] = l1[i-1]

    l1[0] = last_ele

    return l1

lst = [1,2,3,4,5]
print(Rotate_list_right_by_one_position(lst))