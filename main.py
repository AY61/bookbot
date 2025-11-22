from stats import word_split, stats
import sys

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

def get_book_text(filepath):
    output = filepath.read()
    return output

def print_out(letter_dictionary, words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("--------- Character Count -------")
    for thing in letter_dictionary:
        if thing.isalpha():
            print(f"{thing}: {letter_dictionary[thing]}")
    print("============= END ===============")
    

def main():
    with open(book) as f:
        text = get_book_text(f)
        words = word_split(text)
        letter_stats = stats(text)
        print_out(letter_stats, words)
        #print(letter_stats)

main()