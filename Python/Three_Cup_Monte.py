from random import shuffle
def shuffle_list(my_list):
    result= shuffle(my_list)
    return result

def user_guess():
    guess=''
    while guess not in ["0","1","2"]:
        guess=input("Enter any one number:  0 , 1 , 2  :")
      
    return int(guess)

def winOrLose(my_list,user_input):
    if my_list[user_input]=="O":
        
        return "Winner!!!!!!!"
    else:
        return "Sorry, You Lost!!!!!!!!"
       
my_list= [" ","O", " "]
shuffle_list(my_list)
input= user_guess()
ans= winOrLose(my_list,input)
print(ans)
print(my_list)
