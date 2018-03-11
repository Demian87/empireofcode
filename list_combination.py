def list_combination(list1, list2):
    i = 0
    result = list()
    while i < len(list1) or i < len(list2):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
        i+=1
    return result

if __name__ == '__main__':
    assert list_combination([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6], "First"
    assert list_combination([1, 1, 1, 1], [2, 2, 2, 2]) == [1, 2, 1, 2, 1, 2, 1, 2], "Second"

    print("All set? Click \"Check\" to review your code and earn rewards!")
