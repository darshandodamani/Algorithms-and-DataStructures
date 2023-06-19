import quick_sort
import count_sort

def main():
    #different inputs for quick_sort
    arr1 = [0, 21, -8, 1, 6, 5, 3, 19, 7]
    arr2 = [1, 43, 2, 20, -5, 6, 48, 7, 9]
    arr3 = [9, 57, 7, 16, 15, 4, 3, 12, 1]
    # Sorting using Quicksort
    quick_sort.quick_sort(arr1, 0, len(arr1)-1)
    quick_sort.quick_sort(arr2, 0, len(arr2)-1)
    quick_sort.quick_sort(arr3, 0, len(arr3)-1)

    print("Quicksort:")
    print("Sorted arr1:", arr1)
    print("Sorted arr2:", arr2)
    print("Sorted arr3:", arr3)

    #different inputs for count_sort
    arr4 = [54, 21, 8, 1, 6, 5, 3, 19, 7]
    arr5 = [1, 43, 2, 20, 5, 6, 48, 7, 9]
    arr6 = [9, 57, 7, 16, 15, 4, 3, 12, 1]

    # Sorting using Countsort
    count_sort.count_sort(arr4)
    count_sort.count_sort(arr5)
    count_sort.count_sort(arr6)

    print("\nCountsort:")
    print("Sorted arr4:", arr4)
    print("Sorted arr5:", arr5)
    print("Sorted arr6:", arr6)

if __name__ == '__main__':
    main()