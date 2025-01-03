def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = word_count(file_contents)
    chars = char_count(file_contents)
    print_report(words, chars)

def word_count(file):
    return len(file.split())

def char_count(file):
    char_count = {}
    for char in file.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_report(words, chars):
    char_dict = {}
    for key, value in chars.items():
        if key.isalpha():
            char_dict[key] = value
    sorted_chars = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for key, value in sorted_chars.items():
        print(f"The '{key}' character was found {value} times")


main()