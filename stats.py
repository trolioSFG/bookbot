
def count_words(text):
    return len(text.split())

def count_characters(text):
    lower_text = text.lower()
    count = {}

    for char in lower_text:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    return count

def sort_on(dict):
    return dict["num"]

def sort_count(count):
    list_count = []

    for char in count:
        list_count.append({"char": char, "num": count[char]})

    list_count.sort(reverse=True, key=sort_on)

    return list_count
