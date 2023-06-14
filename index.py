def find_word(word, text):
    occurrences = []
    words = text.split()
    
    for i in range(len(words)):
        if words[i] == word:
            occurrences.append(i)
    
    return occurrences

user_word = input("Enter the word to find: ")
user_text = input("Enter the text: ")

found_indices = find_word(user_word, user_text)

if found_indices:
    print(f"The word '{user_word}' was found at the following indices: {found_indices}")
else:
    print(f"The word '{user_word}' was not found in the text.")
