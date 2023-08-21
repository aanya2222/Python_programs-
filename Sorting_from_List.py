def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

# Input: List of numbers
num_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

insertion_sort(num_list)

print("Sorted list using insertion sort:", num_list)