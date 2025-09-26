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

            return filename, word_count
    except FileNotFoundError:
        return None
   
    """We close the file when we are not using it anymore"""
    file.closed
True

words_in_file = count_words('The_Zen_of_Python.txt')

print(words_in_file)