def Find_duplicate_elements_in_string_list(lst):
    duplicate=[]
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count+=1
        if count>1 and lst[i] not in duplicate:
            duplicate.append(lst[i])
    return duplicate

print(Find_duplicate_elements_in_string_list(["java","python","java"]))