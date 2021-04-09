"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) == 0:
        return array
    # take last element as a pivot
    pivot_pos = len(array) -1
    pivot_val = array[pivot_pos]
    
    i = 0
    while i < pivot_pos and pivot_pos -1 > 0:
        if array[i] >= array[pivot_pos]:
            above_val = array[i]
            pre_pivot_val = array[pivot_pos -1]
            # do the shifts and the exchanges :
            array[i] = pre_pivot_val
            array[pivot_pos-1]= pivot_val
            array[pivot_pos]= above_val
            pivot_pos -= 1
        else:
            i += 1
    # end of while : Pivot value is at its right position.
    # Now need to split left array and right array of pivot
    # and apply quicksort on each splitted arrays.
    # and then join the results together.
    left_array = array[0:pivot_pos]
    right_array = array[pivot_pos+1:]
    #print(f'left:{left_array} pivot:{pivot_val} right:{right_array}')
    #print('left:{} pivot:{} right:{}'.format(left_array,pivot_val,right_array))
    left_array = quicksort(left_array)
    right_array = quicksort(right_array)
    result = left_array
    result.append(pivot_val)
    result.extend(right_array)
    
    return result

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)