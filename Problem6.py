string = "I am a teacher and I love to inspire and teach people"
# Splitting the given string
words_str = string.split(" ")
counts = dict()
unique_words = []
# using for loop checking each element in list is unique or any duplicates are present in list
for word in words_str:
    if word in unique_words:
        counts[word] = counts[word] + 1
    else:
        # Assiging 1 to each unique word and finding length from it
        counts[word] = 1
print("No of Unique words:", len(counts))
