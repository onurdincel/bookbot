def get_num_words(file_content):
    return len(file_content.split())

def get_num_chars(file_content):
    char_dict = {}

    for c in file_content:
        c_lower = c.lower()

        if c_lower not in char_dict:
            char_dict[c_lower] = 1
        else:
            char_dict[c_lower] += 1

    return char_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_chars(file_content):
    
    char_dict = get_num_chars(file_content)
    char_array = []

    for k, v in char_dict.items():
        char_array.append({"char": k,"num": v})
    char_array.sort(reverse=True, key=sort_on)
    return char_array
