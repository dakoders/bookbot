def get_num_words(file_contents):
    split = file_contents.split()
    return len(split)

def get_character_count(text):
    characters = {}
    for character in text:
        lowered = character.lower()
        if lowered not in characters:
            characters[lowered] = 1
        else:
            characters[lowered] += 1
    return characters




def sort_by_value(dict):
    list_values = []
    for char in dict:
        list_values.append({"char": char, "count": dict[char]})
    def sort_on(item):
        return item["count"]
    list_values.sort(reverse=True, key=sort_on)
    return list_values
