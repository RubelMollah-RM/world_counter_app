def count_words(word_list, file):

    with open('text.txt', 'r') as file:
        file_words = file.read().split()

    word_count = {}

    for word in word_list:
        count = file_words.count(word)
        word_count[word] = count

    return word_count


search_word = ["Python", "Java", "Java", "C",
               "C++", "PHP", "Python", "Java", "OOP"]

file = "text.txt"


result = count_words(search_word, file)


for word, count in result.items():
    print(f"{word} -> {count}")
