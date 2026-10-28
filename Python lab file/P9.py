def clean_text(text):
    return "".join(text.lower().split())


def character_count(text):
    count = {}
    for ch in text:
        count[ch] = count.get(ch, 0) + 1
    return count


def anagram_check(text1, text2):
    text1 = clean_text(text1)
    text2 = clean_text(text2)
    return sorted(text1) == sorted(text2)


def pattern(text):
    count = character_count(clean_text(text))
    return tuple(sorted(count.items()))


text1 = input("Enter first word/phrase: ")
text2 = input("Enter second word/phrase: ")

if anagram_check(text1, text2):
    print("The given texts are Anagrams.")
else:
    print("The given texts are not Anagrams.")

print("\nCharacter Pattern:")
print(pattern(text1))