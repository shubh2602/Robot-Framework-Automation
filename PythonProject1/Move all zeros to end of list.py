def Move_all_zeros_to_end_of_list(lst):
    result = []
    zero_count = 0
    for num in lst:
        if num == 0:
            zero_count+=1
        else:
            result.append(num)

    for i in range(zero_count):
        result.append(0)
    return result

print(Move_all_zeros_to_end_of_list([1,0,2,0,3,0]))