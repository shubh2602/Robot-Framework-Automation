def is_sorted(lst):
    ascend = True
    descend = True
    if (len(lst)<=1):
        return True

    for i in range (len(lst)-1):
            if lst[i]>lst[i+1]:
                ascend = False
            if lst[i]<lst[i+1]:
                descend = False
    return ascend or descend

list = [1,2,3,4,5]
if is_sorted(list):
    print("List is sorted")
else:
    print("List is not sorted")