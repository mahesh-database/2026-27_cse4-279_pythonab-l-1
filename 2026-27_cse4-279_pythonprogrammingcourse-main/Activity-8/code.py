
import string

# Step 1: Read a paragraph from the user
paragraph = input("Enter a paragraph: ")

# Step 2: Convert the paragraph into lowercase
paragraph = paragraph.lower()

# Step 3: Remove punctuation marks
for symbol in string.punctuation:
    paragraph = paragraph.replace(symbol, "")

# Step 4: Split the paragraph into words
words = paragraph.split()

# Step 5: Create an empty list to store repeated words
repeated_words = []

# Step 6: Display the heading
print("\nRepeated Words and Their Positions:")

# Step 7: Check each word in the paragraph
for word in words:

    # Count the occurrences of the word
    count = words.count(word)

    # Check whether the word occurs more than once
    if count > 1 and word not in repeated_words:

        # Store the repeated word
        repeated_words.append(word)

        # Create a list to store word positions
        positions = []

        # Find all positions of the repeated word
        for i in range(len(words)):
            if words[i] == word:
                positions.append(i + 1)

        # Display the word, count and positions
        print(f"{word} - Count: {count}, Positions: {positions}")
