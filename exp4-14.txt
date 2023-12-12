def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Get input from the user for the percentage data
percentage_array = []
num_students = int(input("Enter the number of students: "))

for student_index in range(1, num_students + 1):
    percentage = float(input(f"Enter the percentage for Student {student_index}: "))
    percentage_array.append(percentage)

# Sorting using Selection Sort
selection_sort(percentage_array)
print("Sorted Array using Selection Sort:", percentage_array)

# Sorting using Bubble Sort
bubble_sort(percentage_array)
print("Sorted Array using Bubble Sort:", percentage_array)
