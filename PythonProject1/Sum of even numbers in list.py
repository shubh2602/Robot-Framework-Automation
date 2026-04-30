def Sum_of_even_numbers_in_list(lst):

    even_sum = 0

    for i in lst:
        if i % 2 == 0:
            even_sum += i

    return even_sum

list1 = [1,2,3,4,5]
print("sum - ",Sum_of_even_numbers_in_list(list1))