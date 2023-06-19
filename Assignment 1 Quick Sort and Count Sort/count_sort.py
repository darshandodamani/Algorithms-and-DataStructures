import numpy as np

def count_sort(input_arr):
    key = int(max(input_arr))
    output_arr = np.zeros(len(input_arr), dtype=int)
    count = np.zeros(key+1, dtype=int)

    for j in range(0, len(input_arr)):
        count[input_arr[j]] += 1
        
    for i in range(1, key+1):
        count[i] += count[i-1]

    for j in range(len(input_arr)-1, -1, -1):
        output_arr[count[input_arr[j]]-1] = input_arr[j]
        count[input_arr[j]] -= 1

    for i in range(0, len(input_arr)):
        input_arr[i] = output_arr[i]

    return input_arr