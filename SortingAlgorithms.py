class Sorts:
    def BubbleSort(self, data):
        states = []

        def bubble_sort():
            n = len(data)
            for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                    if data[j] > data[j + 1]:
                        data[j], data[j + 1] = data[j + 1], data[j]
                        swapped = True
                        states.append([data.copy(), j * (i + 1)])  # Add current state and index
                if not swapped:
                    break

        bubble_sort()
        return states

    def InsertionSort(self, data):
        states = []

        def insertion_sort():
            n = len(data)
            for i in range(1, n):
                key = data[i]
                j = i - 1
                while j >= 0 and key < data[j]:
                    data[j + 1] = data[j]
                    j -= 1
                    states.append([data.copy(), j * (i + 1)])  # Add current state and index
                data[j + 1] = key
                if j >= 0:
                    states.append([data.copy(), (j + 1) * (i + 1)])  # Record position of final insert

        insertion_sort()
        return states

    def SelectionSort(self, data):
        states = []

        def selection_sort():
            n = len(data)
            for i in range(n):
                min_idx = i
                for j in range(i + 1, n):
                    if data[j] < data[min_idx]:
                        min_idx = j
                if min_idx != i:
                    data[i], data[min_idx] = data[min_idx], data[i]
                    states.append([data.copy(), j * (i + 1)])  # Add state and index of the swap

        selection_sort()
        return states

    def QuickSort(self, data):
        states = []

        def quick_sort(low, high):
            if low < high:
                pi = partition(low, high)
                quick_sort(low, pi - 1)
                quick_sort(pi + 1, high)

        def partition(low, high):
            pivot = data[high]
            i = low - 1
            for j in range(low, high):
                if data[j] < pivot:
                    i += 1
                    data[i], data[j] = data[j], data[i]
                    states.append([data.copy(), i])  # Add state and index of the swap
            data[i + 1], data[high] = data[high], data[i + 1]
            states.append([data.copy(), j * (i + 1)])  # Pivot swap
            return i + 1

        quick_sort(0, len(data) - 1)
        return states

    def MergeSort(self, data):
        states = []  # This will store the entire array at each merge step

        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)  # Recursively sort the left half
                merge_sort(right_half)  # Recursively sort the right half

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1
                    # Capture the entire array after each merge operation
                    states.append([arr.copy(), j * (i + 1)])

                # If there are remaining elements in left_half
                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1
                    # Capture the entire array after each merge operation
                    states.append([arr.copy(), j * (i + 1)])

                # If there are remaining elements in right_half
                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1
                    # Capture the entire array after each merge operation
                    states.append([arr.copy(), j * (i + 1)])

        merge_sort(data)  # Start the merge sort on the original array
        return states
