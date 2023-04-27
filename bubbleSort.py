"""
Bubble Sort:
[-2, 45, 0, 11, -9]

[(-2, 45), 0, 11, -9]

[-2, (45, 0), 11, -9]

[-2, 0, (45, 11), -9]

[-2, 0, 11, (45, -9)]

[(-2, 0), 11, -9, 45]

[-2, (0, 11), -9, 45]

[-2, 0, (11, -9), 45]

[-2, 0, -9, (11, 45)]

[(-2, 0), -9, 11, 45]

[-2, (0, -9), 11, 45]

[-2, -9, (0, 11), 45] 

[-2, -9, 0, (11, 45)]

[(-2, -9), 0, 11, 45]

[-9, (-2, 0), 11, 45]

[-9, -2, (0, 11), 45]

[-9, -2, 0, (11, 45)]

[-9, -2, 0, 11, 45]

Sorting in ascending order
"""

list = [-2, 45, 0, 11, -9]

def bubbleSort(list):
    # cant make a comparison on the last number of the list, bc there isnt a number after it
    length = len(list) -1
    # local variable to use throughout this function
    sorted = False

    # using a while True loop bc we dont know how many times we need to loop
    while not sorted:
        sorted = True
        for i in range(0, length):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    return list

print(bubbleSort(list))

# Worst Case O(n^2)
# Space Complexity O(1)
# Worst Case:  O(n^2) Descending order bc bubble sort sorts in ascending order
# Best Case: O(n) array is already sorted
# Avg Case: O(n^2) Elements of the array are jumbled order
# Space Complexity: O(1)
# Bubble Sort is effective when the array elements are few and the array is nearly sorted