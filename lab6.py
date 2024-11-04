import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(book_list:list[data.Book])->None:
    if(book_list != []):
        for i in range(len(book_list) - 1):
            min_idx = i
            for j in range(i + 1, len(book_list)):
                if book_list[j].title.lower() < book_list[min_idx].title.lower():
                    min_idx = j
                if min_idx != i:
                    temp = book_list[i]
                    book_list[i] = book_list[min_idx]
                    book_list[min_idx] = temp


# Part 2
def swap_case(string:str)->str:
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string
# Part 3
def str_translate(string:str,old:str,new:str)->str:
    new_string = ""
    for char in string:
        if char == old:
            new_string += new
        else:
            new_string += char
    return new_string

# Part 4
def histogram(string:str)->dict:
    word_list = string.split()
    dict = {}
    for word in word_list:
        if(word in dict):
            dict[word] += 1
        else:
            dict[word] = 1

    return dict