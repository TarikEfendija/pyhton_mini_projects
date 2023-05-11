print("Welcome to special quiz!")
print("Rules are simle. You'll be placed in 3 teams. Winer is team with highest score")

Team_one_score=0
Team_two_score=0
Team_three_score=0
Score_list=[0,0,0]
First_question= print("First question is: Which movie is the best?)
First_answer= "harry potter"
Team_one_first_answer=input("Team one, answer is: ").lower()
Team_two_first_answer=input("Team teo, answer is: ").lower()
Team_three_first_answer= input("Team three, answer is: ").lower()

if Team_one_first_answer== First_answer:
    print("Bravo Team one")
    Score_list[0] += 1
else:
    print("Team one answer isn't correct")

if Team_two_first_answer == First_answer:
    print("Bravo Team two")
    Score_list[1] += 1
else:
    print("Team two answer isn't correct")


if Team_three_first_answer == First_answer:
    print("Bravo Team three")
    Score_list[2] += 1
else:
    print("Team three answer isn't correct")


Secound_question= print("Prvo pitanje glasi:'Koji je najbolji glumac?")
Secound_answer= "harry"
Team_one_secound_answer=input("Team one, answer is: ").lower()
Team_two_secound_answer=input("Team teo, answer is: ").lower()
Team_three_secound_answer= input("Team three, answer is: ").lower()

if Team_one_secound_answer== Secound_answer:
    print("Bravo Team one")
    Score_list[0] += 1
else:
    print("Team one answer isn't correct")

if Team_two_secound_answer == Secound_answer:
    print("Bravo Team two")
    Score_list[1] += 1
else:
    print("Team two answer isn't correct")


if Team_three_secound_answer == Secound_answer:
    print("Bravo Team three")
    Score_list[2] += 1
else:
    print("Team three answer isn't correct")

print("Team with highest score is: Team " + str(     Score_list.index(       max(Score_list)      )+1     )   )