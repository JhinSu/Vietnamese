from string import punctuation
import codecs

# Sorts words by alphabetical order with the count as a secondary key
def sort_words(x, y):
    return compared(x[1], y[1]) or compared(y[0], x[0])

# Words to be listed 
Number = 50
words = {}

# Parses file line by line, removing all punctuation, and splits each word 
words_gen = (word.strip(punctuation).lower() for line in codecs.open("dialogue.txt", encoding = 'utf-8') 
                                             for word in line.split())

# Parses through each word in                                           
for word in words_gen:
    words[word] = words.get(word, 0) + 1

# Sorts the words 
top_words = sorted(words.iteritems(), compared=sort_items, reverse=True)[:Number]

# Prints out the top words in the file
for word, frequency in top_words:
    print "%s: %d" % (word, frequency)
