def Find_common_elements_in_two_lists(l1, l2):

    common_ele = []

    for item in l1:
        if item in l2:
            common_ele.append(item)

    return common_ele

l1 = [1,2,3,4]
l2 = [4,3,1,2]

print(Find_common_elements_in_two_lists(l1, l2))