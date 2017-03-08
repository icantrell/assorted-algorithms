def mergesort(arr):
    if len(arr)>1:
        lower_arr = mergesort(arr[:len(arr)/2])
        upper_arr = mergesort(arr[len(arr)/2:])
        new_arr = []
        while lower_arr or upper_arr:
            if not lower_arr:
                return new_arr + upper_arr
            elif not upper_arr:
                return new_arr + lower_arr
            elif lower_arr[0] < upper_arr[0]:
                new_arr.append(lower_arr.pop(0))
            else:
                new_arr.append(upper_arr.pop(0))
        return new_arr    
    else:
        return arr

print mergesort([2,6,4,3,45,6,7,34])
