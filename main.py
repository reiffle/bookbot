def main():

    book_path="books/frankenstein.txt"
    book_text=get_text(book_path)
    lowered_book = book_text.lower()
    char_dict=charcount(lowered_book)
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount(book_text)} words found in the document")
    print() # Empty line
    new_list=reverse(char_dict)
    new_list.sort(reverse=True)
    for entry in new_list:
        print(f"The '{entry[1]}' character was found {entry[0]} times")
    print("--- End report ---")
      

def wordcount(text):
    words = len(text.split())
    return words

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
