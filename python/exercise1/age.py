print("---feature age calculater---")

age = int(input("please inter your age :"))
print("your curent age :",age)
age= age +5 
print(f"youcer future age is :{age}")
if age >= 18 :
    print("you are allowed")
else: 
    print("access denied")
for i in range(1,6):

    print(f"Year is : {i}") 


i = 1
while i <= 5 :
    print(i)
    i=i+1

count = 0
for i in range(1,11):
    print(i*i)
    count = count + 1 
print(f"count is {count}")

largest = None 
for n in range(1,11) : 
    if largest is None or n > largest :
        largest = n 
print('largest', largest)

shortest = None
for n in range(1,11):
    if shortest is None or shortest > n:
        shortest = n 
print("shortest is", shortest)


