from random import randint

print("Guess the Number betwen 1 and 20")

nb_to_guess = randint(1, 20)
#print (nb_to_guess)

print ("Choose how many turns")
turns = int(input())
i = 0
win = False
while i < turns:
    print("Turn n° " + str(i + 1))
    player_choice = int(input())
    if player_choice > nb_to_guess:
        print("Too high")
    elif player_choice < nb_to_guess:
        print("Too Low")
    else :
        print ("Well done !")
        win = True
        break
    i = i + 1 
if win == False:
    print("you loose !")
