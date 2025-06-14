from stats import *

def get_book_text(path):

    with open(path) as file:
        return file.read()



def main():
    content = get_book_text("books/frankenstein.txt")

    num = num_of_words(content)

    #print(num)

    #print(convert_to_dict(content))

    lst = sort_dict(convert_to_dict(content))



    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")


    for dct in lst:
        if dct["character"].isalpha():
            print(f"{dct["character"]}: {dct["num"]}")
        else:
            continue

    print("============= END ===============")





main()
