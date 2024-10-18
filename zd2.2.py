def sort_words_by_length(words):
    return sorted(words, key=len)

words = input("Введите слова через пробел: ").split()
print(sort_words_by_length(words))