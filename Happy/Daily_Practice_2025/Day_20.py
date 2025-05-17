l1 = ["is", "are", "then", "that"]
l2 = ['t', 'a', 'i', 's', 'e', 'r']

# Function to check if a word can be formed from the available characters
def can_form_word(word, char_list):
    temp_list = char_list.copy()  # Create a copy of the list to avoid modifying the original
    for char in word:
        if char in temp_list:
            temp_list.remove(char)  # Remove the used character
        else:
            return False  # If character not found, word can't be formed
    return True

# Check each element in l1
results = {}
for word in l1:
    results[word] = can_form_word(word, l2)

# Print the results
for word, can_form in results.items():
    if can_form:
        print(f"'{word}' can be formed using l2 elements.")
    else:
        print(f"'{word}' cannot be formed using l2 elements.")