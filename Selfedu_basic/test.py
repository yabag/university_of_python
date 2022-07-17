
lst = list(map(str.lower, input().split()))
text_set = {word for word in lst}
text_dict = {word: lst.count(word) for word in text_set}

print(text_dict['и'] if 'и' in text_dict else 0)
