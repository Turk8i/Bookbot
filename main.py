from stats import num_of_words

def get_book_text(path):

    with open(path) as file:
        return file.read()



def main():
    content = get_book_text("books/frankenstein.txt")

    num = num_of_words(content)

    print(f"{num} words found in the document")




main()
