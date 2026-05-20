def Find_missing_number_from_list(lst):
    for i in range(1, len(lst)+2):
        if i not in lst:
            return i
        
print(Find_missing_number_from_list([1,2,4,5]))