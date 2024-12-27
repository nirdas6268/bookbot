def main():
    book_path = "books/frankenstein.txt"
    text = text_Read(book_path)
    num_text_words = num_words(text)
    unique_char_count = count_alphabet_unique(text)
    chars_sorted_list = chars_dict_to_sorted_list(unique_char_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_text_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def text_Read(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def num_words(text):
    return len(text.split())

def count_alphabet_unique(text):
    alphabet_dict = {}
    for char in text:
        char_lowered = char.lower()
        if char_lowered in alphabet_dict:
            alphabet_dict[char_lowered] += 1
        else:
            alphabet_dict[char_lowered] = 1
    
    return alphabet_dict

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()