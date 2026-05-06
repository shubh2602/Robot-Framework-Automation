def remove_duplicates(list):
    unique_list = []

    for num in list:
        if num not in unique_list:
            unique_list.append(num)

    return unique_list

numbers = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(numbers)
print(result)