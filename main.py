def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    dict_to_print = count_chars(text)
    #print(dict_to_print)
    create_a_report(num_words, dict_to_print)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_chars(text):
    text_to_lower = text.lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    dict_of_letters = {}
    for i in range(len(letters)):
        dict_of_letters[letters[i]] = text_to_lower.count(letters[i])
    return dict_of_letters

def create_a_report(num_of_words, characters_dict):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{num_of_words} words found in the document')
    print(' ')
    sorted_dict = dict(sorted(characters_dict.items(), key= lambda item: item[1], reverse=True))
    for k,v in sorted_dict.items():
        if k != ' ':
            print(f"The '{k}' character was found in {v} times")
    print('--- End report ---')


main()