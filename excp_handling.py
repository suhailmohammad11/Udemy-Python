#Problem-1
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("These cannot be multiplied, Sorry!!")
    
#Problem-2
x = 5
y = 0

try:

    z = x/y
except ZeroDivisionError:
    print("Hey, This is not possible to divide !!!")
    
#Problem-3
def ask():
    while True:
        try:
            inp=int(input("Input an integer: "))
        except:
            print("An error occured! please try Again!")
        else:
            sq=inp**2
            print("Thank You, Your number squared is ",sq)
            break
ask()
        