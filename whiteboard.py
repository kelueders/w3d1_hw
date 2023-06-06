# Shortest Word

# Given a string of words, return an array of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

# Example Input: words = "Will bitcoin take over the world maybe who knows perhaps"
# Example Output: ['the', 'who']

# Example Input: words = "so long and thanks for all the fish"
# Example Output: ['so']

# split the string into separate words
# loop through the list and find the length of each word
# also in that loop find the shortest length by setting shortest_length to float("inf")
# if statement to print the words at the corresponding indices of th

def shortest_word(sentence):
    word_list = sentence.split()
    word_lengths = []
    for word in word_list:
        word_lengths = append(len(word))
    print(word_length)


shortest_word("Will bitcoin take over the world maybe who knows perhaps")