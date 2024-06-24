def myfunc(*args):
    list1=[]
    for num in args:
        if num%2==0:
            list1.append(num)
    return list1
res= myfunc(-2,4,6,4,5,7)
print(res)       


def lesser_of_two_even(n1,n2):
    if n1%2==0 and n2%2==0:
        if n1>n2 :
            return n2
        else:
            return n1
    elif n1%2!=0 or n2%2!=0:
        if n1>n2:
            return n1
        else:
            return n2
ans=lesser_of_two_even(2,5)
print(ans)    
        
        
def animal_crackers(text):
   words=text.split()
   if len(words)<2:
       return False
   
   if words[0][0]==words[1][0]:
       return True
   else:
       return False

answer=animal_crackers("Suhail Shaik")
print(answer)


def makes_twenty(n1,n2):
    if n1+n2 == 20 or n1==20 or n2==20:
        return True
    else:
        return False
res=makes_twenty(18,2)
print(res)
        
        
def old_macdonald(name):
    name1=[]
    for i in range(len(name)):
        if i==0 or i==3:
            name1.append(name[i].upper())
        else:
            name1.append(name[i].lower())
    return ''.join(name1)
    
name="macdonald"
result1=old_macdonald(name)
print(result1)            

def master_yoda(text):
    words=text.split()
    rev=[]
    for word in words:
        rev.append(word)
    
    return " ".join(rev[::-1])

rever=master_yoda("I am home")
print(rever)

def paper_doll(text):
    
    for index in range(len(text)):
        print(text[index] *3 , end="")
        
paper_doll("Missiissippii\n")


 #spy_game([1,2,4,0,0,7,5]) --> True
 #spy_game([1,0,2,4,0,5,7]) --> True
 #spy_game([1,7,2,0,4,5,0]) --> False
 
def spy_game(my_list):
    code=[0,0,7]
    emp=[]
    for item in my_list:
        if item in code:
            emp.append(item)
    if emp==code:
        return True
    else:
        return False
        
            
q=spy_game([1,2,0,3,0,7,4])
print(q)