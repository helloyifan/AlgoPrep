import sys

hashMapSeen = {}

# Requirement Collection
# Multiple File Solution
# 2 Files (should be extandable to any number)
# input is only lowercase alphabetic characters

#file2 = open("cache/p2.txt", "r")


# Key: Tuple that shows starting and ending characters
# example (0, 13), (14, 26)
# we will use ord(c), 97 is a in ord
# we will use 0 as 'a'

# Value: File path to the file
keyMap = {
    (0, 13): "cache/p1.txt",
    (14, 26): "cache/p2.txt",
}

## expanable key system
## If we use first two character to hash which file it goes to
# (s1, e1, s2, e2)

# (s1, e1, s2, e2, s3, e3)
# "abc"

for line in sys.stdin:
    # Req 1 santize input
    santizedLine = line.replace("\n", "")

    # Req 2 check to see which file the string should be in
    firstCharOrdVal = ord(santizedLine[0]) - 97

    identifiedKey = None
    for i, e in enumerate(keyMap):
        if firstCharOrdVal >= e[0] and firstCharOrdVal <= e[1]:
            identifiedKey = e

    if identifiedKey == None:
        raise("We didnt find any cache file to put this in")


    # Req 3 check to see if the string is in that file
    readFile = open(keyMap[identifiedKey], "r") 
    
    flagToSeeIfStringIsInFile = False
    for lineFromFile in readFile:
        sanitzedLineFromFile = lineFromFile.replace("\n", "")
        if santizedLine == sanitzedLineFromFile:
            flagToSeeIfStringIsInFile = True

    # Req 4b.So we saw in in the file, do nothing
    if flagToSeeIfStringIsInFile:
        print("DEBUG: dup found")
        continue

    # Req 4a: if string is not in that file, add to file and print
    appendFile = open(keyMap[identifiedKey], "a")
    appendFile.write(santizedLine + '\n')
    appendFile.close()

    print(santizedLine)

print("Ctrl-D has been pressed")
