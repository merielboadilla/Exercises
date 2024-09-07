# Program to calculate the length of a string.
print("\nTask 1: Calculate the length of a string")

def calculate_length(s):
    return len(s)

string = "Hello, Meriel!"
print("Length of the string:", calculate_length(string))

# Expected Output: Length of the string: 14 (spaces and punctuation are counted)


# Program to count the number of characters in a string.
print("\nTask 2: Count the number of characters in a string")

def count_characters(s):
    return len(s)

string = "ohayo gozaimasu"
print("Number of characters in the string:", count_characters(string))

# Expected Output: Number of characters in the string: 15 (includes spaces)


# Program to modify a string by replacing all occurrences of its first character 
# with '$', except for the first occurrence.
print("\nTask 3: Replace all occurrences of the first character with '$' except the first occurrence")

def change_char(s):
    first_char = s[0]
    s = s.replace(first_char, '$')
    s = first_char + s[1:]  # Keep the first occurrence of the character
    return s

string = "preparing"
print("Modified string:", change_char(string))

# Expected Output: Modified string: prepa$ing (all 'p's except the first are replaced)


# Program to swap the first two characters of two strings and concatenate them.
print("\nTask 4: Swap the first two characters of two strings and concatenate")

def swap_and_concatenate(m, p):
    new_m = p[:2] + m[2:]  # Replace the first two characters of the first string with the second string's first two
    new_p = m[:2] + p[2:]  # Replace the first two characters of the second string with the first string's first two
    return new_m + ' ' + new_p

string1 = "love"
string2 = "hate"
print("Swapped and concatenated string:", swap_and_concatenate(string1, string2))

# Expected Output: Swapped and concatenated string: have lote (first two letters are swapped)


# Program to concatenate four strings with spaces in between.
print("\nTask 5: Concatenate four strings with spaces")

a = "Hello"
b = "everyone"
c = "from"
d = "Tunasan"
concatenated_string = a + " " + b + " " + c + " " + d
print("Concatenated string:", concatenated_string)

# Expected Output: Concatenated string: Hello everyone from Tunasan


# Program to form a sentence using a name and age.
print("\nTask 6: Create a sentence using a name and age")

name = "Meriel"
age = 21
paragraph = "My name is " + name + " and I am " + str(age) + " years old."
print(paragraph)

# Expected Output: My name is Meriel and I am 21 years old.


# Program to concatenate two user-input strings with a space in between.
print("\nTask 7: Concatenate two user-input strings")

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
concatenated_string = string1 + " " + string2
print("Concatenated string:", concatenated_string)

# Expected Output: Concatenated string will depend on the input provided by the user.
