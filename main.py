def mergeTwoLists(list1, list2):
    # Indexes referring to one list each
    index1 = 0
    index2 = 0
    merged_list = []

    while True:
        # I don't already merge an entire list
        if index1 < len(list1) and index2 < len(list2):
            # I have to add the element of list1 and increment the relative index
            if list1[index1] <= list2[index2]:
                merged_list.append(list1[index1])
                index1 += 1
            # I have to add the element of list1 and increment the relative index
            elif list1[index1] > list2[index2]:
                merged_list.append(list2[index2])
                index2 += 1
        # List1 is all merged, I have to add all the list2 (is already ordered
        elif index1 == len(list1):
            # Cycling to all remaining elements
            for index2 in range(index2, len(list2)):
                merged_list.append(list2[index2])
            break
        # List2 is all merged, I have to add all the list1 (is already ordered
        else:
            # Cycling to all remaining elements
            for index1 in range(index1, len(list1)):
                merged_list.append(list1[index1])
            break
    return merged_list


assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
