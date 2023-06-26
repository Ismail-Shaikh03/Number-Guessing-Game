import random
counter=0
a_i=int(random.randint(0,51))
player=int(input("Guess the number 1-50, you have 5 tries!:"))
counter+=1
while counter<=5:
    if player < a_i:
        print("Value is too low!")
        player=int(input("Guess again!"))
        counter+=1
    elif player > a_i:
        print("Value is too high!")
        player=int(input("Guess again!"))
        counter+=1
    elif player == a_i:
        print("You got the right answer!")
        break
    if counter>=5:
        print("You ran out of attempts!")
        break
