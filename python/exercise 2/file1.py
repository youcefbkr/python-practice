print("---Text file analyser---")

filename = 'text.txt'

try :
    file = open(filename,"r")
    text = file.read()
    file.close()
except FileNotFoundError:
    print("file not found")
    exit()

if not text.strip():
    print("text is empty")
    exit()

char_count = len(text)
print("number of charcters is :", char_count)

words = text.split()
print("Words:", words)
 
words_count = len(words)
print("number of words :", words_count)


largest = None 
for word in words : 
    if largest is None or len(largest) < len(word):
        largest = word 
print("the largest word is :", largest )


shortest = None
for word in words : 
    if shortest is None or len(shortest) > len(word):
        shortest = word 
print("the shortest word is ", shortest)