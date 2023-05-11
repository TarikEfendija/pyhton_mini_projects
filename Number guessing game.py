#Program witch generate a random number and track how many times it takes the user to guess the number

import random

top_of_range=input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger then 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number= random.randint(0, top_of_range) #mogli koristiti i .randrange stim da tada pyhton ne bi uključivao donnju i gornju granicu

guesses=0

while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        
    else:
        print("Please type a number next time.")
        continue
    if user_guess > top_of_range: #On je radio bez ovog, a ja sam dodao ovo. 
        print("You have to type smaller number then first.")
        continue
    if user_guess==random_number:
        print("You got it.")
        break
     #Ako želimo da damo hint da li smo iznad ili ispod random broja, to radimo na način da unutar ovog elsa ubacimo... 
     #if user_guess > random_number: print("...")
     #else: print("...")
     #Ili dodamo elif umjesto if-a
    else:
        print("You got it wrong.")
print("You got it in", guesses, "guesses.")

#Drugi način
#While True:
    #guesses +=1
    #user_guess = input("Make a guess: ")
    #if user_guess.isdigit():
    #    user_guess=int(user_guess)
        
    #else:
        #print("Please type a number next time.")
        #continue
    #if user_guess > top_of_range:
        #print("You have to type smaller number then first.")
        #continue
    #elif user_guess == random_number:
        #print("You got it.")
    #elif user_guess > random_number:
        #print("You are above random number.")
    #else:
        #print("You are below random number.")