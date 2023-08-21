def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)

print(f"Number of vowels in the string: {vowel_count}")