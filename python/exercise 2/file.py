print("--- Exercie 2 ---")



filename = "text.txt"

try :
    file = open(filename , "r")
    text = file.read()
    file.close()
except FileNotFoundError:
    print("file is not found")
    exit()

if not text.strip():
    print("file is empty")
    exit()

char_count = len(text)
print("number of charcter is :", char_count)

words = text.split()
print("Words", words)

words_count = len(words)
print("number of words is ", words_count)

largest = None

for word in words:
    if largest is None or len(largest) < len(word) :
        largest = word
print("largest is ",largest)

shortest = None 
for word in words:
    if shortest is None or len(shortest) > len(word) :
        shortest = word 
print("shortest is :", shortest)