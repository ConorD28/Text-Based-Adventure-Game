# Final Project.py
# A program that is designed to run an adventure game called Joe's Journey, which is about a person named Joe trying to escape a strange building. The game can be played multiple times.
# by: Conor Desmond
# Date: 05/28/2021

def first_door(score1):
    times_wrong = 0 #initializes times_wrong to 0. This varibale will keep track of how many times a user answers a question incorrectly.
    times_correct = 0 #initializes times_correct to 0. This varibale will keep track of how many times a user answers a question correctly.
    
    while times_wrong < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("What is the capital of Montana?")
        print("A) Helena")
        print("B) Cheyenne")
        print("C) Tallahassee")
        print("D) Olympia")
        ans1 = input("Type the letter corresponding to the correct answer for this question and the rest of the questions you answer on the touchscreens in this building.").lower()
 
        if ans1 == "a": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score1 = score_and_messages(times_correct, times_wrong, score1) #calls function to adjust score and print a message and sets score1 equal to the score returned from the function.
            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score1 = score_and_messages(times_correct, times_wrong, score1) #calls function to adjust score and print a message and sets score1 equal to the score returned from the function.

    if times_wrong < 2: #checks to see if the user has answered the first question wrong less than 2 times.
        times_wrong = 0 #resets times_wrong to 0 before moving onto the next question.
        times_correct = 0 #resets times_correct to 0 before moving onto the next question.
        
    while times_wrong < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("What is the capital of Florida?")
        print("A) Helena")
        print("B) Albany")
        print("C) Tallahassee")
        print("D) Bismarck")
        ans2 = input().lower()

        if ans2 == "c": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score1 = score_and_messages(times_correct, times_wrong, score1) #calls function to adjust score and print a message and sets score1 equal to the score returned from the function.
            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score1 = score_and_messages(times_correct, times_wrong, score1) #calls function to adjust score and print a message and sets score1 equal to the score returned from the function.

        
    if times_wrong < 2: #checks to see if the user has answered the second question wrong less than 2 times.
        times_wrong = 0 #resets times_wrong to 0 before moving onto the next question.
        times_correct = 0 #resets times_correct to 0 before moving onto the next question.
        
    while times_wrong  < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("What is the capital of South Dakota?") 
        print("A) Concord")
        print("B) Baton Rogue")
        print("C) Pierre")
        print("D) Bismarck")
        ans3 = input().lower()

        if ans3 == "c": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score1 = score_and_messages(times_correct, times_wrong, score1) #calls function to adjust score and print a message and sets score1 equal to the score returned from the function.

            print("A button comes up on the screen that says 'unlock'. Joe presses the button. The door unlocks and Joe walks up to the touchscreen next to the next door.")
            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score1 = score_and_messages(times_correct, times_wrong, score1) #calls function to adjust score and print a message and sets score1 equal to the score returned from the function.


    return score1, times_wrong

def score_and_messages(times_correct2, times_wrong2, total_score):
    if times_correct2 == 1:
        print("Correct.")
        total_score = total_score + 1 #The variable total_score will eventually hold the value of the final score
        
    elif times_wrong2 == 1:
        print("Incorrect. Try again")
        if total_score > 0:
            total_score = total_score - 1
            
    if times_wrong2 == 2:
        print("Incorrect.")
        if total_score > 0:
            total_score = total_score - 1

    return total_score

def second_door(score2):
    times_wrong = 0 #sets times_wrong to 0 before moving onto the next question.
    times_correct = 0 #sets times_correct to 0 before moving onto the next question.
    
    while times_wrong  < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("A question on the touchscreen comes up: When programming using the programming language called Python, what symbol should be typed between two different strings")
        print("to concatenate them?")
        print("A) +")
        print("B) -")
        print("C) *")
        print("D) ~")
        ans1 = input().lower()

        if ans1 == "a": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score2 = score_and_messages(times_correct, times_wrong, score2) #calls function to adjust score and print a message and sets score2 equal to the score returned from the function.

            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score2 = score_and_messages(times_correct, times_wrong, score2) #calls function to adjust score and print a message and sets score2 equal to the score returned from the function.


    if times_wrong < 2: #checks to see if the user has answered the first question associated with the second door wrong less than 2 times.
        times_wrong = 0 #resets times_wrong to 0 before moving onto the next question.
        times_correct = 0 #resets times_correct to 0 before moving onto the next question.

    while times_wrong < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("When programming using the programming language called Python and assuming the math library has been imported in already, how does one take the natural log of x?")
        print("A) math.log(x)")
        print("B) math.log10(x)")
        print("C) ceil(x)")
        print("D) math.ln(x)")
        ans2 = input().lower()

        if ans2 == "a": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score2 = score_and_messages(times_correct, times_wrong, score2) #calls function to adjust score and print a message and sets score2 equal to the score returned from the function.

            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
           times_wrong = times_wrong + 1
           score2 = score_and_messages(times_correct, times_wrong, score2) #calls function to adjust score and print a message and sets score2 equal to the score returned from the function.


    if times_wrong  < 2: #checks to see if the user has answered the second question associated with the second door wrong less than 2 times.
        times_wrong = 0 #resets times_wrong to 0 before moving onto the next question.
        times_correct = 0 #resets times_correct to 0 before moving onto the next question.
    
    while times_wrong  < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("When programming using the programming language called Python and assuming the math library has been imported in already, how does one take the inverse sin of x?")
        print("A) math.sin^-1(x)")
        print("B) cos(x)")
        print("C) math.arcsin(x)")
        print("D) math.asin(x)")
        ans3 = input().lower()

        if ans3 == "d": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score2 = score_and_messages(times_correct, times_wrong, score2) #calls function to adjust score and print a message and sets score2 equal to the score returned from the function.

            print("A button comes up on the screen that says 'unlock'. Joe presses the button. The door unlocks and Joe walks up to the touchscreen next to the next door.")
            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score2 = score_and_messages(times_correct, times_wrong, score2) #calls function to adjust score and print a message and sets score1 equal to the score returned from the function.

    return score2, times_wrong

def third_door(score3):
    times_wrong = 0 #sets times_wrong to 0 before moving onto the next question.
    times_correct = 0 #sets times_correct to 0 before moving onto the next question.
      
    while times_wrong < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("A question on the touchscreen comes up: What number is supposed to fill in the blank according to the following pattern?")
        print("1 1 2 1 1 3 2 2 2 1 2 2 6 1 1 1 2 1 1 9 2 _")
        print("A) 1")
        print("B) 2")
        print("C) 3")
        print("D) 4")
        ans1 = input().lower()

        if ans1 == "b": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score3 = score_and_messages(times_correct, times_wrong, score3) #calls function to adjust score and print a message and sets score3 equal to the score returned from the function.

            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score3 = score_and_messages(times_correct, times_wrong, score3) #calls function to adjust score and print a message and sets score3 equal to the score returned from the function.


    if times_wrong < 2: #checks to see if the user has answered the first question associated with the third door wrong less than 2 times.
        times_wrong  =  0 #resets times_wrong to 0 before moving onto the next question.
        times_correct = 0 #resets times_correct to 0 before moving onto the next question.

    while times_wrong  < 2: #checks to see if the user has answered the question wrong less than 2 times
        print( "1 1 5 1 1 5 7 6 5 1 4 5 0 1 5 1 4 5 1 2 _")
        print("What number is supposed to fill in the blank according to the pattern?")
        print("A) 2")
        print("B) 3")
        print("C) 4")
        print("D) 5")
        ans2 = input().lower()

        if ans2 == "d": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score3 = score_and_messages(times_correct, times_wrong, score3) #calls function to adjust score and print a message and sets score3 equal to the score returned from the function.

            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score3 = score_and_messages(times_correct, times_wrong, score3) #calls function to adjust score and print a message and sets score3 equal to the score returned from the function.


    if times_wrong  < 2: #checks to see if the user has answered the second question associated with the third door wrong less than 2 times.
        times_wrong = 0 #resets times_wrong to 0 before moving onto the next question.
        times_correct = 0 #resets times_correct to 0 before moving onto the next question.
     
    while times_wrong < 2: #checks to see if the user has answered the question wrong less than 2 times
        print( "1 1 3 0 0 2 2 2 4 0 0 2 3 3 5 0 0 2 4 4 _?")
        print("What number is supposed to fill in the blank according to the pattern?")
        print("A) 0")
        print("B) 2")
        print("C) 5")
        print("D) 6")
        ans3 = input().lower()

        if ans3 == "d": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score3 = score_and_messages(times_correct, times_wrong, score3) #calls function to adjust score and print a message and sets score3 equal to the score returned from the function.

            print("A button comes up on the screen that says 'unlock'. Joe presses the button. The door unlocks and Joe walks up to the touchscreen next to the next door.")
            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score3 = score_and_messages(times_correct, times_wrong, score3) #calls function to adjust score and print a message and sets score3 equal to the score returned from the function.

            
    return score3, times_wrong

def fourth_door(score4):
    times_wrong = 0 #sets times_wrong to 0 before moving onto the next question.
    times_correct = 0 #sets times_correct to 0 before moving onto the next question.
    
    while times_wrong  < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("A question on the touchscreen comes up: What is an atoll?")
        print("A) A toll")
        print("B) a ring-shaped reef, island, or chain of islands made up of coral.")
        print("C) a strip of land that is narrow and has sea on either side of it. It forms a link between two larger areas of land.")
        print("D) a group of islands.")
        ans1 = input().lower()

        if ans1 == "b": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score4 = score_and_messages(times_correct, times_wrong, score4) #calls function to adjust score and print a message and sets score4 equal to the score returned from the function.

            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score4 = score_and_messages(times_correct, times_wrong, score4) #calls function to adjust score and print a message and sets score4 equal to the score returned from the function.

        
    if times_wrong  < 2: #checks to see if the user has answered the first question associated with the fourth door wrong less than 2 times.
           times_wrong  =  0 #resets times_wrong to 0 before moving onto the next question.
           times_correct = 0 #resets times_correct to 0 before moving onto the next question.
           
    while times_wrong  < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("What is an isthmus?")
        print("A) a strip of land that is narrow and has sea on either aside of it. It forms a link between two larger areas of land.")
        print("B) a ring-shaped reef, island, or chain of islands made up of coral.")
        print("C) A group of hills.")
        print("D) a group of islands.")
        ans2 = input().lower()

        if ans2 == "a": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score4 = score_and_messages(times_correct, times_wrong, score4) #calls function to adjust score and print a message and sets score4 equal to the score returned from the function.

            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score4 = score_and_messages(times_correct, times_wrong, score4) #calls function to adjust score and print a message and sets score4 equal to the score returned from the function.

            
    if times_wrong < 2: #checks to see if the user has answered the second question associated with the fourth door wrong less than 2 times.
           times_wrong = 0 #resets times_wrong to 0 before moving onto the next question.
           times_correct = 0 #resets times_correct to 0 before moving onto the next question.
        
    while times_wrong < 2: #checks to see if the user has answered the question wrong less than 2 times
        print("What is an archipelago?")
        print("A) A group of hills.")
        print("B) a strip of land that is narrow and has sea on either side of it. It forms a link between two larger areas of land.")
        print("C) An extremely deep valley.")
        print("D) a group of islands.")
        ans3 = input().lower()

        if ans3 == "d": #checks if the user answered the question correct
            times_correct = times_correct + 1
            score4 = score_and_messages(times_correct, times_wrong, score4) #calls function to adjust score and print a message and sets score4 equal to the score returned from the function.

            break #breaks out of the while loop so the question does not get asked again after the user answers the question correctly
        else:
            times_wrong = times_wrong + 1
            score4 = score_and_messages(times_correct, times_wrong, score4) #calls function to adjust score and print a message and sets score4 equal to the score returned from the function.


    return score4, times_wrong

def game_over(final_score): #function that prints an ending message, asks the user about playing again, and returns the answer to the question about playing again.
    print("Game Over. Joe is trapped inside the building for the rest of his life. Your final score is", final_score)
    play2 = eval(input("Copyright: Conor Desmond; Conor.Desmond1@marist.edu; Would you like to play again? Type 1 in for Yes and 2 in for No "))

    return play2
    
def main():
    play = 1 #This variable will check if the game should run or not.

    while play == 1:  
        print("A person named Joe wakes up inside a strange building. Joe does not recall how he got inside the building. The last thing he remembers doing was studying")
        print("geography, state capitals, and programming. He sees a door ahead of him and walks up to it. He tries to open the door, but it is locked. Joe is required to go ")
        print("through 4 doors to get out of the building. He is required to answer 3 questions about state capitals to unlock the first door, answer 3 programming questions")
        print("to unlock the second door, fill in 3 blanks with the correct numbers to unlock the third door, and answer 3 geography questions with the correct answers to unlock")
        print("the fourth and final door. He sees a touchscreen next to the door. The touchscreen states, 'The user of this touchscreen and other touchscreens in this building gets")
        print("2 attempts per question. The user gets 1 point per correct answer, and if the user has at least 1 point, a loss of a point per incorrect answer. If the user of this")
        print("device gets a question wrong twice, this door will never unlock. But, if the user gets all three questions right, a button will come up, that if pressed, will unlock")
        input("this door. Push the enter button to begin playing Joe’s Journey.")

        score = 0 #initializes score to zero.
        
        first_score_and_wrong = first_door(score) #calls the function for the first door, sends it the inital score,
                                                  #and sets a variable called first_score_and_wrong equal to the
                                                  #score from the question(s) the user answered associated with the first door and the
                                                  #number of incorrect answers from the user on the last question the user answered associated with the first door.
        
        if first_score_and_wrong[1] < 2: #checks if the last question the user answered associated with the first door was answered incorrectly by the user less than two times.
            second_score_and_wrong = second_door(first_score_and_wrong[0])#calls the function for the second door, sends it the score from the first door,
                                                                          #and sets a variable called second_score_and_wrong equal to the
                                                                          #score from the questions the user answered associated with the first and second door and equal the
                                                                          #number of incorrect answers from the user on the last question the user answered associated with the second door.
            if second_score_and_wrong[1] < 2: #checks if the last question the user answered associated with the second door was answered incorrectly by the user less than two times.
                third_score_and_wrong = third_door(second_score_and_wrong[0]) #calls the function for the third door, sends it the score from the first door,
                                                                              #and sets a variable called third_score_and_wrong equal to the
                                                                              #score from the questions the user answered associated with the first, second, and third door and equal the
                                                                              #number of incorrect answers from the user on the last question the user answered associated with the third door.

                if third_score_and_wrong[1] < 2: #checks if the last question the user answered associated with the third door was answered incorrectly by the user less than two times.
                    fourth_score_and_wrong = fourth_door(third_score_and_wrong[0])#calls the function for the fourth door, sends it the score from the first door,
                                                                                  #and sets a variable called fourth_score_and_wrong equal to the
                                                                                  #score from all the questions the user answered associated with the first, second, third, and fourth door and equal the
                                                                                  #number of incorrect answers from the user on the last question the user answered associated with the fourth door.

                    if fourth_score_and_wrong[1] < 2: #checks if the last question the user answered associated with the fourth door was answered incorrectly by the user less than two times.
                        print("Congratulations, Joe has escaped the building! The game is over. Your final score is", fourth_score_and_wrong[0])
                        play = eval(input("Copyright: Conor Desmond; Conor.Desmond1@marist.edu; Would you like to play again? Type 1 in for Yes and 2 in for No "))
                    else:
                        play = game_over(fourth_score_and_wrong[0]) #calls game_over function and sets play equal to the value returned from the function
                else:
                    play = game_over(third_score_and_wrong[0]) #calls game_over function and sets play equal to the value returned from the function
            else:
                play = game_over(second_score_and_wrong[0]) #calls game_over function and sets play equal to the value returned from the function
            
        else:
            play = game_over(first_score_and_wrong[0]) #calls game_over function and sets play equal to the value returned from the function

main()

#used Oxford Dictionaries for some some information
