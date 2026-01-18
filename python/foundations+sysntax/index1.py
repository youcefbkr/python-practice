print("before")
for value in [42,12,43,65,86,2,1,5,6,8,9,23,4]:
    if value > 20 :
        print("number abouve 20 ", value)
    else:
        print("number below 20 ", value)
print("after")
found = False 
print("before found is",found)
for values in [1,2,3,4,5,6,7,8,9,12,3,32,54,4,57,6,3]:
    if values == 54 :
        found = True
    print(found, values)
print("after", found)