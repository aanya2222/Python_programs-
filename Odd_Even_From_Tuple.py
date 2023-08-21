def check_odd_even(numbers_tuple):
    odd_numbers = []
    even_numbers = []

    for num in numbers_tuple:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return odd_numbers, even_numbers

# Input: Tuple of numbers
num_tuple = tuple(int(x) for x in input("Enter a tuple of numbers separated by spaces: ").split())

odd_numbers, even_numbers = check_odd_even(num_tuple)

print("Odd numbers in the tuple:", odd_numbers)
print("Even numbers in the tuple:", even_numbers)