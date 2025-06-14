from stats import num_of_words, convert_to_dict

def get_book_text(path):

    with open(path) as file:
        return file.read()



def main():
    content = get_book_text("books/frankenstein.txt")

    num = num_of_words(content)

    #print(num)

    print(convert_to_dict(content))





main()
