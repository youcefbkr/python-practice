print("--- File analyser ---")
filename = 'text.txt'
try:
    file = open(filename,"r")
    text = file.read()
    file.close()
except FileNotFoundError:
    print(" File not found")
    exit()

if not text.strip():
    print("file is empty")
    exit()

char_count = len(text)
print(f"number of characters : {char_count}")
words = text.split()
words_count = len(words)
print(f"number of words : {words_count}")

longest = None
for word in words :
    if longest is None or len(word) > len(longest):
        longest = word
print("longest word is ", longest)

shortest = None
for word in words :
    if shortest is None or len(word) < len(shortest):
        shortest = word

print("shortest word is :", shortest)
