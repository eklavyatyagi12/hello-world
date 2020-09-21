print("made by eklavya tyagi")
lose = "computer wins"
win = "you win"
lives = 5
score = 0
drew = 0
computer_lives = 7
while True:
    print("to begin fill the information")
    username = input("please enter username:   ")
    password = input("please enter password:   ")
    searchfile = open("account.csv","r")
    for line in searchfile:
        if username and password in line:
            print("access granted")
            print("live rules")
            print("you start with",lives,"lives")
            print("if you win you get extra life")
            print("if you lose you lose a life")
            print("if you draw,the lives stay the same")
            print("-----------------------------------------------------------------------------------------------------")
            print("MAKE SURE YOU DONT USE CAPITAL LETTERS")
            print("-----------------------------------------------------------------------------------------------------")
            print("to see a list of rules")
            print("-----------------------------------------------------------------------------------------------------")
            print("to leave the game, type exit")
            print("can you beat the computer")
            print("GOOD LUCK!!!!  ")
            print("-----------------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("     ___                  ______________     ______________     _______________     ____      ___                                        ")
            print("    ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /                                           ")
            print(" /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /                                            ")
            print("/            \     ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /                                             ")
            print("¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /                                              ")
            print("¦       ------------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /                                               ")
            print("¦            \     ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \                                               ")
            print("¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \                                              ")
            print("¦       ------------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___    ")
            print("¦            \     ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦       ")
            print("¦       ------------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦       ")
            print("\       ------------ ___________     _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       ")
            print(" \           \     /¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       ")
            print("  \---------------/ ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       ")
            print("                    ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       ")
            print("                    ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /       ")
            print("                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /        ")
            print("                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /         ")
            print("                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /                                _____")
            print("                    ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                                /     /")
            print("                                                                                                                                                                 /     /")
            print(" ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________                    /     /")
            print("¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ________    /     /")
            print("¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /          /     /")
            print("¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦         /     /")
            print("¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /")
            print("             ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               __________________")
            print("             ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                                 ¦")
            print(" ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               __________________¦")
            print("¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦")
            print("                                                                                                                                                                                                  ")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            while True:                
                rps = input("rock,paper,scissors?   ")
                import random
                computer = ("rock","paper","scissors")
                computer = random.choice(computer)
                #rock if statements
                if rps == "rock" and computer == "paper":
                    print("the computer choose",computer)
                    print("  ")
                    print(lose)
                    print("  ")
                    print("  ")
                    lives -= 1
                if rps == "rock" and computer == "scissors":
                    print("the compter choose",computer)
                    print("  ")
                    print(win)
                    computer_lives -=1
                    print("  ")
                    score +=1

                #paper if statements
                if rps == "paper" and computer == "rock":
                    print("the computer choose",computer)
                    print("  ")
                    print(win)
                    computer_lives -=1
                    print("  ")
                    print("  ")
                    score += 1
                if rps == "paper" and computer == "scissor":
                    print("the computer choose",computer)
                    print("  ")
                    print(lose)
                    print("  ")
                    print("  ")
                    lives -= 1

                #scissor if statements
                if rps == "scissors" and computer == "paper":
                    print("the computer choose",computer)
                    print("  ")
                    print(win)
                    computer_lives -= 1
                    print("  ")
                    print("  ")
                    score += 1
                if rps == "scissors" and computer == "stone":
                    print("the computer choose",computer)
                    print("  ")
                    print(lose)
                    print("  ")
                    print("  ")
                    lives -= 1

                #duplicate entries
                if rps == "rock" and computer == "rock":
                    print("the computer chooses",computer)
                    print("  ")
                    print("you drew")
                    print("  ")
                    print("  ")
                    drew += 1
                if rps == "paper" and computer == "paper":
                    print("the computer choose", computer)
                    print("  ")
                    print("you drew")
                    print("  ")
                    print("  ")
                    drew += 1
                if rps == "scissors" and computer == "scissors":
                    print("the computer choose", computer)
                    print("  ")
                    print("you drew")
                    print("  ")
                    print("  ")
                    drew += 1
                #system
                if rps == "rules":
                    print("******************************************************")
                    print("rules")
                    print("******************************************************")
                    print("rock loses against paper")
                    print("rock wins agaisnt scissors")
                    print("paper beats rock")
                    print("paper loses against scissors")
                    print("scissors wins agaisnt paper")
                    print("scissors loses agaisnt rock")
                    print("*****************************************************")
                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print(score)
                if rps == "display drew" :
                    print(drew)

                #lives
                if lives == 0 or rps == "test":
                    print("thanks for playing")
                    print("you have ran out of chances")
                    print(" you got",score,"correct")
                    print("you drew",drew,"times")
                    stop = input("press enter to exit")
                    import time
                    time.sleep(0.5)
                if computer_lives == 0:
                     print("thanks for playing")
                     print("the computer lost all its lives")
                     print("you got",score,"correct")
                     print("you drew", drew,"times")
                     stop = input("press enter to exit")
                     import time
                     time.sleep(0.5)
                #exit
                if rps == "exit":
                    break
                
    else:
      print("your username or password is incorrect")
      print("--------------------------------------------------------------------------------------------------")
                
                          


                 
























                                
                          
                          
                    






                          
                    
            
            





