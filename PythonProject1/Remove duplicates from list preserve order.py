def Remove_duplicates_from_list_preserve_order(str):

    result = ""

    for num in str:
        if num not in result:
            result += num

    return result

str1 = "Hello"
print(Remove_duplicates_from_list_preserve_order(str1))