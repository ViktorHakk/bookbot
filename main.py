import sys
if len (sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import count, print_characters, count_characters
print ("============ BOOKBOT ============")
print (f"Analyzing book found at {sys.argv[1]}")
print ("----------- Word Count ----------")
print (f"Found {count(sys.argv[1])} total words")
print ("--------- Character Count -------")
print_characters(sys.argv[1])
print ("============= END ===============")
