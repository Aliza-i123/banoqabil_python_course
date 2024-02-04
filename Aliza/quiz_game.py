# Aliza Roshan
# roshanaliza177@Gmail.com
# Quiz Game



# All Questions
questions = ("How my keys are there on keyboard?: ",
                       "What is the full form of CPU?: ",
                       "What is the full form of ROM?: ",
                       "When was computer invented?: ",
                       "Computer was invented by?: ")

#All Options

options = (("A. 116", "B. 117", "C. 104", "D. 119"),
                   ("A. Central Processing Unit", "B. Center Progress Underline", "C. Central Program Unit", "D. None Of These"),
                   ("A. Read only memory", "B. Reading of Memory", "C. Bothh A & B", "D. None of These"),
                   ("A. 1606", "B. 1750", "C. 1947", "D. 1837"),
                   ("A. William Shakespare", "B. Charles Babbage", "C. Bill Gates", "D. Elon Musk"))

answers = ("C", "A", "D", "A", "B")
guesses = []
score = 0
question_num = 0

# Printing the matter

for question in questions:
    print("__________________________________")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ")
    guesses.append(guess)

# If and Else Condition

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("\nBEST OF LUCK FOR YOUR NEXT PROJECT")

