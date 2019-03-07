import random
num_array=[]
print("Enter the number of times you want to play the game")
num=int(input())
for i in range(num):
    num_array.append(random.randrange(1,4)) 
print(" 1 denotes stone \n 2 denotes paper\n 3 denotes scissor")
#print(num_array)
c=0
print("Enter your choices")
for j in range(num):
    user_input = int(input())
    if user_input==num_array[j]:
        c=c
        print("It's a tie!")
    if (num_array[j] == 1 and user_input == 3):
        print("You loose")
        c=c
    elif(num_array[j] == 1 and user_input == 2):
        print("You win!")
        c=c+1
    elif(num_array[j] == 2 and user_input == 1):
        print("You loose")
        c=c
    elif(num_array[j] == 2 and user_input == 3):
        print("woah! you win!")
        c=c+1
    elif(num_array[j] == 3 and user_input == 1):
        print("You win!")
        c=c+1
    elif(num_array[j] == 3 and user_input == 2):
        print("you loose")
        c=c
print("You won the game for times:")
print(c)

     
     
        
