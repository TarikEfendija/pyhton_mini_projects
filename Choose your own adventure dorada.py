#Chooseing game
print("Hi! I'm Dobby a free elf. I'll be your guide through this game. What is your name?")
name = input("My name is: ")
print("Welcome", name, "I'll hope that you'll enjoy.")

print("First od all do you want to download game or you'll play on this site? (Options: download/play)")
answer=input("").lower()
bag=[]
if answer == "download":
    print("Thank you for downloading. For the prize you get the key, use it wisely!")
    bag.append("key")
elif answer == "play":
     print("Ok! Let's play.")
else:
    print("This isn't valid option. You lose.")

print("You are young wizard and you find yourself in a time when Lord Voldemort is trying to regain all his power. You were looking for herbs for healing potion when you heard Draco Malfoy say...")
print("Draco: Soon Lord Vodlemort will regain all his power and now, when Dumbledore is dead, there is no wizard who can stop him.")
print("What will you do about it? (Options: think/ignore)")

answer=input("").lower()
if answer =="think":
    print("You thought about Draco's words and realised that Lord Voldemort search for the Elder wand. What will you do? (Options: looking for Elder wand/stay in school")
    answer=input("").lower()
    if answer == "looking for Elder wand".lower():
        print("To find the Elder wand you have to get some information about it. Where you will look for information about it: in library or at Olivander's?(Options: library/olivander's)")

        answer=input("").lower()
        if answer == "library":
            print("You search tons of books and found out many useful informations but one sentence is particulary stuck in your memory:'The bloody trail of the Elder Wand is splattered across the pages of Wizarding history'. But you couldn't figured out the meaning of that sentence, so you need someone to interpret that sentence for you. Who will you ask: (Options:)professor Snape or professor McGonagall.")
            answer=input("").lower()
            if answer == "professor snape":
                print("Professor Snape told you that you have more important things to focus on.")
            elif answer == "professor mcgonagall":
                print("Professor McGonagall explained to you that if you want to be master of the Elder wand you have to kill current master.")
                print("After that she asked you reason why you were looking for the meaning of those words. Will you tell her about your little adventure. (Options: yes/no)")
                answer=input("").lower()
                if answer == "yes":
                    print("Professor McGonagall: 'Thats very noble and dangerous adventure. I'll give you one advice:the secrets of the dead are buried with them.")
                    print("You realised that the Elder wand is buried whit Dumbledore. But no one knows where is he buried.")
                    print("Sad you walk down the hall because you failed to complete a task when suddenly a room of requirement appears in front of you. Do you want to enter into room?(Options: yes/no)")
                    answer=input("").lower()
                    if answer=="yes":
                        print("You entered in the room and found the Mirror of Erised. You looked in the mirror and see the Great Lake and tomb in the middle of it.")
                        print("You found Dumbledore's grave. Suddenly a map and the Invisibility Cloak appears in your hands. Now you have all you need to save the world.")
                        bag.append("map")
                        bag.append("the invisibility cloak")
                        print("You used map you get in the room of requirements to find Dumbledore's tomb. On the Dumbledore's tomb it says:'You need the key to open the tomb'.")
                        print("Do you have key in your bag?")
                        if "key" in bag:
                            print("You unlocked the tomb and found the Elder wand. Congratulations", name, "you saved the world.")
                        else:
                            print("You don't have a key. Lord Voldemort found you at the tomb. He killed you. You should download the game.")
                    elif answer =="no":
                        print("The room od requirements disappears. You are a coward. Game over.")
                    else:
                        print("This isn't valid option. You lose.")
                elif answer == "no":
                    print("After McGonagall explanation you still don't know meaning od that sentence")
                    print("Your research takes too long. Lord Voldemort finds the Elder wand before you. Game over.")
                else:
                    print("This isn't valid option. You lose.")
            
            else:
                print("This isn't valid option. You lose.")
        elif answer == "olivander's":
            print("When you arrived at Olivander's the Death Eaters attacked the shop and kill you by accident. Game over.")
        else:
            print("This isn't valid option. You lose.")
    elif answer == "stay in school":
        print("Lord Voldemort regain his power and attacked the school. You died hiding in an abandoned part of the castle. Trol sat on you")
    else:
        print("This isn't valid option. You lose.")

elif answer == "ignore":
    print("After a while Lord Voldemort regain his power and attacked the school. Your healing potion has done you no good, you were killed by the Dead Eater.")
else:
    print("This isn't valid option. You lose.")