def quick_sort(A, p, r):                 #calling quicksort (A, 1,A.len)
    #p: starting index of the subarray
    #r: ending index of the subarray
    if p < r:
        q = partition(A, p, r)          #partitioning the array
        quick_sort(A, p, q-1)            #quicksorting the left subarry
        quick_sort(A, q+1, r)            #quickaorting the right subarray

def partition(A, p, r):
    x = A[r]
    i = p - 1
    # for j in range(p, r-1):
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]     #swaping current elements at index i
    A[i+1], A[r] = A[r], A[i+1]         #swaping elements at index i+1
    return i+1