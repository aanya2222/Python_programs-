def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Input: List of integers
num_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]

unique_numbers = remove_duplicates(num_list)

print("List with unique numbers:", unique_numbers)