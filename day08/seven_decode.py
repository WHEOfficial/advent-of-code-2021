import re

def remove_chars(s, chars):
    pattern = f"[{chars}]"
    return re.sub(pattern, "", s)

def get_correct_segments(inputs):
    len_map = {}
    final_map = {}
    for input in inputs:
        key = str(len(input))
        if key not in len_map:
            len_map[key] = input
        else:
            if type(len_map[key]) != list:
                len_map[key] = [len_map[key]]
            len_map[key].append(input)
    possible_cf = len_map['2']
    
    final_map['a'] = remove_chars(len_map['3'], possible_cf)
    
    possible_bd = remove_chars(len_map['4'], possible_cf)

    strip_string = f"{possible_cf}{final_map['a']}{possible_bd}"

    print(f"STRING: {strip_string}")

    for combo in len_map['5']:
        print(combo, remove_chars(combo, strip_string))    

with open("test_input.txt", 'r') as infile:
    groups = [g.split(" | ") for g in infile.read().splitlines()]
    for group in groups:
        get_correct_segments(group[0].split(" "))