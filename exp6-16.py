def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        greater_than_pivot = [x for x in array[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def top_five(array):
    sorted_array = sorted(array, reverse=True)[:5]
    print("Top Five Scores:", sorted_array)

# Taking first-year student percentages as input
percentage_array = []
n = int(input("Enter the number of students: "))
for i in range(n):
    percentage = float(input(f"Enter percentage for student {i + 1}: "))
    percentage_array.append(percentage)

# Sorting using Quick Sort
sorted_percentage_array = quick_sort(percentage_array)
print("Sorted Array using Quick Sort:", sorted_percentage_array)

# Displaying the top five scores
top_five(sorted_percentage_array)
