# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def chunks(array, n_elements):
    chunks = math.floor(len(array) / n_elements)
    residue = len(array) % n_elements
    main_list = []
    sub_list = []

    # max_index = n_elements * chunks
    start = 0
    end = 0
    for i in range(1, chunks + 1):
        end = i * n_elements

        sub_list = array[start:end]
        main_list.append(sub_list)
        start = end
    if (chunks * n_elements) < len(array):
        sub_list = array[end:end+residue]
        main_list.append(sub_list)
    return main_list


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    n = 10
    list_of_list = chunks(l, n)
    print(list_of_list)


# / --- Directions
# // Given an array and chunk size, divide the array into many subarrays
# // where each subarray is of length size
# // --- Examples
# // chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# // chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# // chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# // chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# // chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
# Visto por Julio Gutiérrez en 1605805958850.

# julio@perfilan.com