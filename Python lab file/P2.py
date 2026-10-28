import string

def analyze_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split text into words
    words = text.strip().split()

    # Count total words
    total_words = len(words)

    # Count frequency of each word
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Find palindrome words
    palindromes = []

    for word in words:
        if len(word) > 1 and word == word[::-1]:
            if word not in palindromes:
                palindromes.append(word)

    # Display results
    print("\n========== TEXT ANALYSIS ==========")
    print("Total number of words:", total_words)

    print("\nWord Frequency:")
    for word, count in sorted(frequency.items()):
        print(word, ":", count)

    print("\nPalindrome Words:")
    if palindromes:
        print(", ".join(palindromes))
    else:
        print("No palindrome words found.")


# Main Program
print("===== Automated Word Frequency & Pattern Analyzer =====")

print("\nEnter your text.")
print("Type 'END' on a new line to finish:")

lines = []

while True:
    line = input()

    if line == "END":
        break

    lines.append(line)

# Join all lines
text = "\n".join(lines)

# Analyze the text
analyze_text(text)

