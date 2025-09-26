
# we define a function that can count words in a defined text file
def count_words(filename):
    try:
        with open(filename, encoding=None) as file:
            text = file.read()

            # Create translation table
            import string
            translator = str.maketrans('', '', string.punctuation)

            # Remove punctuation
            clean_text = text.translate(translator)

            # split into words and count them
            words = clean_text.split()
            word_count = len(words)

            return filename, word_count, clean_text
    except FileNotFoundError:
        return None
   
    """We close the file when we are not using it anymore"""
    file.closed
True

# We run the function and print the output
filename, words_in_file, cleantext = count_words('The_Zen_of_Python.txt')

print(f"File name: {filename}")
print(f"Number of words in the file: {words_in_file}")

#We define a function that can count the frequency of words
def count_word_freqs(cleantext):
    words = cleantext.split()
    frequency = {}
    for word in words:
        word = word.lower().strip(".,!?;:()[]\"'")  # normalize word
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    freq_sorted = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    return freq_sorted

#We run the function and print a list of words and frequencies 
word_frequency = count_word_freqs(cleantext)

print("List of words and their frequency in the file:")
for word, count in word_frequency:
        print(f"{word}, {count}")


