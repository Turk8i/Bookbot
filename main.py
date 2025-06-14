from stats import *
import sys


def get_book_text(path):

    with open(path) as file:
        return file.read()



def main():

    arguements = sys.argv # ["main.py" , ...]

    if len(arguements) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = arguements[1]

    content = get_book_text(path)

    num = num_of_words(content)


    lst = sort_dict(convert_to_dict(content))

 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")


    for dct in lst:
        if dct["character"].isalpha():
            print(f"{dct["character"]}: {dct["num"]}")
        else:
            continue

    print("============= END ===============")

    



main()
