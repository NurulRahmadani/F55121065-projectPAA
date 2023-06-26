def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    arr = [12, 99, 62, 15, 20, 95, 90, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 62, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 74, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    # Bubble Sort
    bubble_sort_arr = arr.copy()
    bubble_sort(bubble_sort_arr)
    print("Hasil Bubble Sort:")
    print(bubble_sort_arr)

    # Insertion Sort
    insertion_sort_arr = arr.copy()
    insertion_sort(insertion_sort_arr)
    print("Hasil Insertion Sort:")
    print(insertion_sort_arr)

if __name__ == '__main__':
    main()