# Given any number of words to unscrable, 
# 

# Sort words by letter, preserving duplicates
# Map of sorted letters to words 
# Sort the given word alpahbetically
# Lookup that sorted string in the map

with open("res/words.txt") as allWords:
    print("Constructing map.")
    sortedMap = dict()
    for line in allWords:
        word = line.strip().lower()
        keyAsList = sorted(word)
        key = "".join(keyAsList)

        if key in sortedMap:
            sortedMap[key].append(word)
        else:
            sortedMap[key] = [word]

print("Map constructed.")

with open("Words to Unscramble") as inputFile:
    print("Solving scrambles.")
    for line in inputFile:
        scramble = line.strip()

        if scramble == "":
            continue

        wordAsList = sorted(scramble)
        word = "".join(wordAsList)
        answer = sortedMap.get(word)
        print(scramble + " - " + str(answer))