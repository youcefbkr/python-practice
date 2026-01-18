def names() :
    print("znji")
    print("Akab")

names()    
def greet():
    return "Hello"
print(greet(), "gleen")
print("hello world")
m = max("boukaraa Youcef") 
print(m)
y = "youcef"
print(f"{m}{ y}")
name = input ('enter your name: ')
print(f'hello {name}')
try :
    age = int(input("please enter your age :"))
    print (f"{age} accepted")
except :
    print("please enter a number")
    age = 0 
age = age+1
print(f"you are {age} years old")
while True:
    try :
        w = int(input("please enter your width :"))
        h = int(input("please enter your hight :"))
        print("access premitted")
        break
    except:
        print("please enter a value")
print(f"your width is {w} your hight is {h}")
area = w*h 
print(f"your area is {area}")
print (f"due to your age which is {age} years old")
if age < 20 :
    print ("access denied")
else :
    print ("access accepted")