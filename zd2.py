def reverse_words(*words):
    return  words[::-1]

words = input("Введите слова через пробел: ").split()
print(reverse_words(words))
