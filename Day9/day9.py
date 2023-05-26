# Write a Python program to check whether an element exists within a tuple

Teams = ("Chelsea","Machester United","Manchester-City","Arsenal")


# print(len(Teams))  

if "Manchester-City" in Teams:
    print("its available in Teams")
else:
    print("not available")


# Write a Python program to convert a list to a tuple
def convert(list):
    return tuple(list)

# driver function

list = [10,20,30,40,50,60,70,80,90,100]
print(convert(list))


aTuple = (100, 200, 300, 400, 500)
aTuple.pop(2)
print(aTuple)


