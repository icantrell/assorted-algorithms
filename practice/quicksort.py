def quicksort(arr):
    if len(arr) <= 2:
        return filter(lambda i:i < arr[len(arr)/2],arr) + filter(lambda i:i >= arr[len(arr)/2],arr)
    else:
        return quicksort(filter(lambda i:i < arr[len(arr)/2],arr)) + quicksort(filter(lambda i:i >= arr[len(arr)/2],arr))

print quicksort([3,4,3,5,6,7,5,1])
    
