def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def count_characters(text):
    character_count = {}
    for i in text.lower():
        if i == " ":
            continue
        elif i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
    return character_count

def sort_on_num(item):
    return item["num"]

def list_of_char_dict(char_dict):
    list_of_char = []
    for i in char_dict:
        list_of_char.append({"char": i, "num": char_dict[i]})
    list_of_char.sort(reverse=True, key= sort_on_num)
    return(list_of_char)
