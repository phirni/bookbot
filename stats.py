def count_words(text):
    words=text.split()
    return len(words)

def count_characters(text):
    character_counts={}
    for char in text:
        char=char.lower()
        
        if char in character_counts:
            character_counts[char] +=1
        else:
            character_counts[char]=1

    return character_counts
def sort_on(dict_item):
    return dict_item["num"]
def sort_characters(character_counts):
    characters_list=[]
    for char, count in character_counts.items():
        characters_list.append({
            "char":char,
            "num":count
            })
        characters_list.sort(reverse=True, key=sort_on)
    return characters_list

