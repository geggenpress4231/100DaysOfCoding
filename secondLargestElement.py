def find_second_largest(arr):
    if len(arr) < 2:
        raise ValueError("Array must have at least two elements.")
    
    max_el = max(arr[0], arr[1])
    second_el = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > max_el:
            second_el = max_el
            max_el = arr[i]
        elif arr[i] > second_el and arr[i] != max_el:
            second_el = arr[i]
    
    if second_el == max_el:
        raise ValueError("No distinct second largest element found.")
    
    return second_el



