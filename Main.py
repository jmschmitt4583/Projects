#Name - Julia Schmitt

#Description of Project - My project is a quiz game, inspired by trivia and the random facts I've learned over the year, as well as some math.
#  The user will answer multiple choice questions and the program will keep track of their score, as well as displaying their score at the end of the program as a fraction and percentage.

#Source Cited
#  Source was used in Sprint 1 to understand difference between elif and else:
#       -Python if ... else. Python Conditions. (n.d.). Retrieved September 18, 2021, from https://www.w3schools.com/python/python_conditions.asp.

#  Source was used in Sprint 2 when working on question_format function in order to have loop repeat when entering an invalid answer:
#       -Cassingena Navone, E. (2020, November 13). Python while loop tutorial – while true syntax examples and infinite loops.
#        freeCodeCamp.org. Retrieved October 29, 2021, from https://www.freecodecamp.org/news/python-while-loop-tutorial/. 

#Introduction
name = input("Hello user! Before we get started, what is your name?: ")
print("Nice to meet you ", name + "! ", end = '')
# string operator + used to concatenate string to where there is no space between name variable and the exclamation point.
print("This program is a trivia quiz meant to test your knowledge on", "really, " * 2 + "random topics ", end = '')
#used string repition operator to doube the string "really, " twice.
print("consisting of 9 questions.", "\nPlease input your answer as A, B, or C!", "Good luck!", sep = '\n')
#end= used to join both print lines, sep= used to place line breaks inbetween strings.
print("_" * 50)
#used string multiplier to create seperating line from introduction to question 1



#Starting score of 0 for function 'quetion_format(correct_answer)' to build off of.
score = 0


def question_format(correct_answer):
#My function definition, used to format questions to avoid having to make minor corrections to each of the 9 questions.
#The Parameter (correct_answer) is used to compare the correct answer of each question with the user_answer that gets input in the function.
    global score
#Used "global" to keep a consistent score after function is completed, instead of having the score return to 0
    while True:
#Added while so that function can repeat input if user makes an error, while 'True' is so that unless the user is able to input one of the options as A, B, or C, the function input will loop around.
        user_answer = input("\nAnswer: ")
        if user_answer.lower() not in ('a', 'b', 'c'):
#If statement to weed out any invalid answers, .lower() was used to register lowercase letters, and 'not' and 'in' keywords were used to include a, b, c in in the if statement as well as other invalid answers.
            print("Invalid Answer. Please make sure to enter capital A, B, or C.")
        elif user_answer == correct_answer:
            print("Congratulations! You chose the correct answer!")
            score = score + 1
#Adding onto the total score when the answer is correct.
            break
#Break used to end the 'While True' loop, loop is only needed for invalid answers.
        elif user_answer == 'A' or 'B' or 'C':
            print("Sorry, your answer was incorrect!")
            break
        else:
            print("Invalid input, please enter A, B, or C.")
#Else used as a catch all statement in case a user input manages to get past other conditions.
    return score

def line_break():
    print("_" * 50)
    #print(score)
#Adds line breaks after each question to seperate them visually. Score was also added to line_break while I was testing the program to make sure the score changed as it was supposed to.

#Question 1
correct_answer = 'A'
print("\nQuestion 1:","Which of these animals isn’t a rodent?", "A. Rabbit", "B. Squirrel", "C. Beaver", sep = '\n')
question_format(correct_answer)
print("Rabbits aren’t rodents because they have four incisors in the upper jaw, while rodents only have two! Instead, they are classified as lagomorphs.")
line_break()


#Question 2
correct_answer = 'B'
print("\nQuestion 2:", "What is one of the leading creators of the white sand that is found on many tropical beaches?", "A. Ocean Salt", "B. Fish Poop", "C. Crustacean Shells", sep = '\n')
question_format(correct_answer)
print("Parrotfish eat coral from reefs, and when the coral comes out the other end, we are left with the white grains of sand that make up 80% of white tropical beaches.")
line_break()


##Question 3
correct_answer = 'B'
print("\nQuestion 3:", "Approximately how many blimps are still in existence as of 2021?", "A. 8 blimps", "B. 25 blimps", "C. 130 blimps", sep = '\n')
question_format(correct_answer)
print("Approximately 25 blimps are in existence, only half of which are still actively used for advertising purposes.")
line_break()

#Question 4
correct_answer = 'C'
print("\nQuestion 4:", "How many national flags have the color purple on them?", "A. 14 National Flags", "B. 6 National Flags", "C. 2 National Flags", sep = '\n')
question_format(correct_answer)
print("There are only two national flags with the color purple, the flags for Dominica and Nicaragua.")
line_break()

#Question 5
correct_answer = 'A'
print("\nQuestion 5:", "What place has had the most lightning strikes in the world?", "A. Lake Maracaibo, Venezuela", "B. City of Teresina, Brazil", "C. Town of Caceres, Colombia", sep = '\n')
question_format(correct_answer)
print("Lake Maracaibo located in Venezuela, receives about 232 lightning strikes in every 247 acres per year.")
line_break()

#Question 6
correct_answer = 'C'
print("\nQuestion 6:", "Which of these fruits takes the longest to grow?", "A. Watermelon", "B. Pineapple", "C. Kiwi", sep = '\n')
question_format(correct_answer)
print("Kiwi plants typically bear fruit between 3-5 years after planting, whereas pineapples average one fruit per 2 years and watermelon 70-90 days to begin fruiting.")
line_break()

#Question 7
correct_answer = 'C'
print("\nQuestion 7:", "How old was the oldest living cat recorded?", "A. 25 Years Old", "B. 32 Years Old", "C. 38 Years Old", sep = '\n')
question_format(correct_answer)
print("The oldest living cat recorded to date was 38 years and three days old! Her name was Crème Puff.")
line_break()

#Question 8
correct_answer = 'A'
print("\nQuestion 8:", "What is the solution to the problem:  2**3-6 ?", "A. 2", "B. 4", "C. 0", sep = '\n')
question_format(correct_answer)
print("The equation comes out to: ", 2**3-6, "!", sep= '')
# ** operator used to create exponet for the problem, - operator used to subtract 6 from the equation.
line_break()

#Question 9
correct_answer = 'B'
print("\nQuestion 9:", "What are the solutions to the problems:  (7//3) and  (7%3) ?", "A.  1, 2", "B.  2, 1", "C. -2, 1", sep= '\n')
question_format(correct_answer)
print("The solution to 7//3 is", (7//3), "and the solution to 7%3 is",(7%3))
# // operator used to do floor division in the solution of the problem listed in the first part of the question dropping the remainder in the division,
# % operator used to get modulus for second part of the problem, using the remainder found in the division.
line_break()

percent = (score/9)*100
#Used operator / to divide total correct from 9, used operator * to multiply by 100 to get percentage.
if score == 9 and percent >= 90:
#Used and to give 2 conditions that have to be met for grade to equal A+
    grade = 'A+'
elif percent >= 90:
    grade = 'A'
elif percent >= 80:
    grade = 'B'
elif percent >= 70:
    grade = 'C'
elif percent >= 60:
    grade = 'D'
else:
    grade = 'F'
#Using if and elif to figure out what letter grade the user recieved on the trivia quiz following normal grading procedures, as usual anything under a 60 is considered an F in the else statement.

#Decided to make different ending displays for those who scored a perfect 100, used if and elif to do so.
if percent != 100:
    print("Nice work ", name, "!", sep = '')
    print("You got ", score, " questions right out of 9, your score ends up coming out at ", format((score/9)*100, '.2f'), "% which means that you ended up with a ", grade, " on this quiz.", sep = '')
#Format was used to add 2 decimal places, and sep was used to remove unnecessary spaces.
elif percent == 100:
    print("Holy cow ", name, "!! You scored a perfect 100%, you must really know youre stuff! A+ for you!", sep = '')
#Changed the way the score was displayed to the user, adding in the letter grade instead of the amount of questions that the user recieved wrong.
print("Thank you for playing this trivia game!")
user_end_answer = int(input("One last question, what's your favorite number 1-10? "))

if user_end_answer > 0 and user_end_answer <= 10:
    print("Okay, then:")
    for x in range (user_end_answer):
#Using range to repeat Goodbye as many times as the number the user entered.
        print("Goodbye!")
    print("See what I did there? Okay but seriously, goodbye!")
elif user_end_answer > 10 or user_end_answer < 0:
#Or keyword used to avoid having to write 2 sperate lines of code for both greater than the top limit and below the bottom limit.
    print("...You are defiant, I can respect that, okay, well goodbye to you and your ", user_end_answer, "!", sep='')
else:
    print("I'm not sure if you meant to type this...but goodbye either way!")
#Old method of scoring the quiz in Sprint 1, keeping on file for review.
    #print("\nNice work ", name, "!\nYou got ", 9 - score, " questions wrong, meaning your score is: ", score, "/9!", sep = '')
    #used operator - to subtract the correct answers from total, which gives the amount of questions that the user got wrong.
    #print("The percentage you received on this quiz is: ", format((score/9)*100, '.2f'), "%", sep = '')
    #used operator / to divide total correct from 9, used operator * to multiply by 100 to get percentage, format was used to add 2 decimal places, and sep was used to remove unnecessary spaces.
    #print("Thank you for playing!")
