# Defining Score variables
x = 0
score = x

# Question One
print("What percent do women fill the positions of directors, writers, producers, executive producers, editors, and cinematographers in 2019-2020?"")
answer_1 = input("a)56%\nb)34%\nc)63%\nd)21%\n:")
if answer_1.lower() == "b" or answer_1.lower() == "34%":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Women fill 34% of film positions in 2019-2020.")
# Each question is formulated in the same way, where there are if and else statements that are dependent on what you enter as your answer.

# Question Two
print("Who is the first female director to win an Oscar?")
answer_2 = input("a)Greta Gerwig\nb)Sophia Coppola\nc)Kathryn Bigelow\nd)Mira Nair\n:")
if answer_2.lower() == "c" or answer_2.lower() == "Kathryn Bigelow":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, in 15.9% of the top-grossing movies, 11% of the cast was a minority.")

# Question Three
print("True or False... 15.9% of the top-grossing movies consisted of casts that were 11% minorities?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Four
print("Who is the highest paid, black actor in Hollywood?")
answer_4 = input("a)Samuel Jackson\nb)Morgan Freeman\nc)Eddie Murphy\nd)Denzel Washington\n:")
if answer_4.lower() == "a" or answer_4 == "Sameuel Jackson":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The highest paid, black actor is Samuel Jackson")

# Question Five
print("Memories of Murder was the first foreign film to win best picture.")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The first foreign film to win best picture was Parasite.")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
# For the final project, I will formulate the code in the same way. I will create twenty questions, along the same lines as what I've set up above.
