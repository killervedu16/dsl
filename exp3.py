def delete_duplicates(books):
    unique_books = []
    for book in books:
        if book not in unique_books:
            unique_books.append(book)
    return unique_books

def ascending_order(books):
    return sorted(books, key=lambda x: x['cost'])

def count_expensive_books(books):
    return sum(1 for book in books if book['cost'] > 500)

def copy_low_cost_books(books):
    return [book for book in books if book['cost'] < 500]

# Get input from the user for the library data
library = []
num_books = int(input("Enter the number of books in the library: "))
for i in range(num_books):
    book_name = input("Enter the name of Book: ")
    book_cost = int(input("Enter the cost of Book: "))
    library.append({'Book': book_name, 'cost': book_cost})

# Delete duplicate entries
unique_library = delete_duplicates(library)

# Display books in ascending order based on cost
sorted_library = ascending_order(unique_library)

# Count number of books with cost more than 500
expensive_books_count = count_expensive_books(sorted_library)

# Copy books with cost less than 500 to a new list
low_cost_books_list = copy_low_cost_books(sorted_library)

# Display results
print("Unique Library:", unique_library)
print("Books in Ascending Order of Cost:", sorted_library)
print("Number of Books with Cost > 500:", expensive_books_count)
print("Books with Cost < 500:", low_cost_books_list)
