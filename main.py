import sys
from stats import wordcount

def main():
    if len(sys.argv) < 2:
        print ("Usage: python 3 main.py <path_to_book>")
        sys.exit(1)
    book_path=sys.argv[1]
    book_text=get_text(book_path)
    lowered_book = book_text.lower()
    char_dict=charcount(lowered_book)
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount(book_text)} words found in the document")
    print() # Empty line
    new_list=reverse(char_dict)
    new_list.sort(reverse=True)
    for entry in new_list:
        print(f"{entry[1]}: {entry[0]}")
    print("--- End report ---")

def charcount(text):
    dictionary = {}
    for x in text:
        lower = x.lower()
        if lower in dictionary:
            dictionary[lower]+=1
        else:
            dictionary[lower]=1
    return dictionary

def reverse(dictionary):
    dictionary_list=[]
    for name in dictionary:
        if name.isalpha():
            new_entry=[dictionary[name], name]
            dictionary_list.append(new_entry)
    return dictionary_list
    

def get_text(path):
    with open(path) as f:
	    return f.read()
         
main()
