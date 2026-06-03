def process_words(words, condition, transform):
    return [transform(word) for word in words if condition(word)]


list1 = ["python", "java", "C++", "JavaScript", "go", "Rust", "Kotlin", "PHP"]

result1 = process_words(list1, lambda word: len(word) > 4, lambda word: word.upper())

print(result1)

result2 = process_words(list1, lambda word: word[0].isupper(), lambda word: len(word))

print(result2)

result3 = process_words(list1, lambda word: 'a' in word, lambda word: word[::-1])

print(result3)
