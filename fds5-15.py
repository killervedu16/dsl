def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

def top_five(array):
    sorted_array = sorted(array, reverse=True)[:5]
    print("Top Five Scores:", sorted_array)

# Taking second-year student percentages as input
percentage_array = []
n = int(input("Enter the number of students: "))
for i in range(n):
    percentage = float(input(f"Enter percentage for student {i + 1}: "))
    percentage_array.append(percentage)

# Sorting using Insertion Sort
insertion_sort(percentage_array)
print("Sorted Array using Insertion Sort:", percentage_array)

# Sorting using Shell Sort
shell_sort(percentage_array)
print("Sorted Array using Shell Sort:", percentage_array)

# Displaying the top five scores
top_five(percentage_array)
