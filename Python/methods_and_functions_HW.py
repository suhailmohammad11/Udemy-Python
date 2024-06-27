#Write a function that computes the volume of a sphere given its radius.
import math
def vol(rad):
    piv=math.pi
    volume=(4/3)*piv*(rad**3)
    return volume
res=vol(4)
print(res)

#Write a function that checks whether a number is in a given range (inclusive of high and low)
#ran_check(5,2,7)
#5 is in the range between 2 and 7

def ran_bool(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False
result=ran_bool(7,2,7)
print(result)

def multiply(list1):
    count=1
    for i in list1:
        count=count*i
    return count
res=multiply([2,3,4])
print(res)

def uniq_list(lst):
    uniq=[]
    for i in lst:
        if i not in uniq:
            uniq.append(i)
    return uniq
lst=[1,1,1,2,3,3,4,4,4,5]
r=uniq_list(lst)
print(r)
        