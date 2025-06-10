# Best structure for camelCase splitter:
# ✅ Version using ord() — your style — with full comments:
def can_split_camel_case(words, camelCase):
    result = []  # to store split words
    word = ""    # temporary word collector

    for char in camelCase:
        # If uppercase letter found (ASCII 65–90)
        if 65 <= ord(char) <= 90:
            # if word already collected, push it to result
            if word:
                result.append(word)
            # start new word by converting to lowercase (ASCII trick)
            word = chr(ord(char) + 32)
        else:
            # just add lowercase char to current word
            word += char

    # add last collected word
    if word:
        result.append(word)

    # check if every word is in the given list
    for w in result:  # result contains the words we split from the camelCase string
      if w not in words:  # if any of them is not in the known words list
        return False
    return True  # all of them were in the list, so it’s valid

example_words = ["apple", "banana", "orange"]
print(can_split_camel_case(example_words, "appleBanana"))  # ✅ True
print(can_split_camel_case(example_words, "appleOrange"))  # ✅ True
print(can_split_camel_case(example_words, "appleWater"))   # ❌ False
