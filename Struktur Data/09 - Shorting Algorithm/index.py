class SortingAlgorithm:
    def __init__(self, data):
        self.data = data

    def bubble_sort(self):
        n = len(self.data)

        for i in range(n):
            # Set flag to check if any swapping occurs in this pass
            swapped = False

            # Last i elements are already sorted, so we don't need to check them
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    # Swap if the element found is greater than the next element
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    swapped = True

            # If no swapping occurs, the array is already sorted
            if not swapped:
                break

    def insertion_sort(self):
        n = len(self.data)

        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j+1] = self.data[j]
                j -= 1
            self.data[j+1] = key

    def selection_sort(self):
        n = len(self.data)

        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def display_sorted_data(self):
        print("Sorted Data:", self.data)

# Contoh penggunaan SortingAlgorithm
data_to_sort = [64, 25, 12, 22, 11]
sorting_algorithm = SortingAlgorithm(data_to_sort)

# Bubble Sort
sorting_algorithm.bubble_sort()
sorting_algorithm.display_sorted_data()

# Insertion Sort
data_to_sort = [64, 25, 12, 22, 11]  # Reset data
sorting_algorithm = SortingAlgorithm(data_to_sort)
sorting_algorithm.insertion_sort()
sorting_algorithm.display_sorted_data()

# Selection Sort
data_to_sort = [64, 25, 12, 22, 11]  # Reset data
sorting_algorithm = SortingAlgorithm(data_to_sort)
sorting_algorithm.selection_sort()
sorting_algorithm.display_sorted_data()