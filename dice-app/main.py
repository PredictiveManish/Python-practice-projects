import random 
repeat = True
while repeat:
    print("You rolled and got: ", random.randint(1,6))
    print("Do you want to role again? Y/N ")
    repeat ="Y" in input()
    
    
    