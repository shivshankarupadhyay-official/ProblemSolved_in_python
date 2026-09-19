
s = "aabbcddee"

def non_repeating_char(s):
    char_count = {}

    # Step 1: Count every character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Step 2: Find the first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    return None


result = non_repeating_char(s)

print(result)
