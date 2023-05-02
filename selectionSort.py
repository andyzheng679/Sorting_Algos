"""
Selction Sort:
[-2, 45, 0, 11, -9]

[(-2), 45, 0, 11, -9]

[(-2), 45, 0, 11, (-9)]

[-9 | 45, 0, 11, -2]

[-9 | (45), 0, 11, -2]

[-9 | (45), (0), 11, -2]

[-9 | 45, (0), 11, (-2)]

[-9, -2 | 0, 11, 45]

[-9, -2 | (0), 11, 45]

[-9, -2, 0 | 11, 45]

[-9, -2, 0 | (11), 45]

[-9, -2, 0, 11 | 45]

[-9, -2, 0, 11, 45]


Trying to find the minimum value, setting the first value as the minimum. 
Then comparing it to every number to the right. When we come across a number that is lower than the minimum, 
we assign that as the new minimum. At the end of the loop, move the minimum to the left. 
Then divide the list into two, the left is the sorted, the right will be the unsorted.
"""

 

list = [-2, 45, 0, 11, -9]


def selectionSort(list):
    #range of the list, len(list)-1 bc if that is the last value in the unsorted list, we can assume it's the highest value
    length = range(0, len(list)-1)
   
    for i in length:
        #first value in the unsorted list to be the min value
        min_value = i

        #for all the values to the right of the min_value
        for j in range(i+1, len(list)):
            if list[j] < list[min_value]:
                min_value = j

        #if we find a value that has a lower value than the original i, then switch the items
        if min_value != i:
            list[i], list[min_value] = list[min_value], list[i]

    return list

print(selectionSort(list))