print("---Text analyser---")
text = input("enter a text:")
if not text.strip():
    print("empty text!program stopped")
    exit()
char_count = len(text)
print("number of charchter :", char_count)
words = text.split()
words_count = len(words)
print("number of words:", words_count)

longest = None
for word in words :
    if longest is None or len(word) > len(longest):
        longest = word
print("longest word:", longest)

shortest =  None
for word in words :
    if shortest is None or len(word) < len(shortest):
       shortest = word 
print("shortest word:", shortest)
