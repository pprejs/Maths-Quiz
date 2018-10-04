#Made by Patryk Prejs
#School Maths Quiz/Test

import random
import operator
x=0

#Welcome Screen
def beginning():
    print("Welcome to the Maths Quiz")
    print("\n1. Play")
    print("\n2. View Previous Games")
    print()
    choice=int(input("What would you like to do?: "))
    if choice==1:
        difficulty()
    else:
        data.previous()

#Player chooses a difficulty
def difficulty():
    modes=(Easy, Advanced)
    print("\n\nChoose a difficulty")
    print("\n1. Easy")
    print("\n2. Advanced")
    print("\n3. Random Equations")
    print("\n\n4. Back to Menu")
    choice=int(input("\nWhat difficulty would you like?: "))
    if choice >4 or choice<1:
        print("Input invalid")
        difficulty()
    elif choice==1:
        Easy()
    elif choice==2:
        Advanced()
    elif choice==3:
        randomequations()
    elif choice==4:
        beginning()
    else:
        print("Thank you")


        
#How i generate a random mathematical expression
def randcalc():
    ops={'+':operator.add,
         '-':operator.sub,
         '*':operator.mul,
         '/':operator.truediv}
    num1=random.randint(0,15)
    num2=random.randint(1,10)
    op=random.choice(list(ops.keys()))
    answer=ops.get(op)(num1,num2)
    print("What is {} {} {}?\n".format(num1, op, num2))
    return answer

#Getting the program to ask the user
def askuser():
    answer=randcalc()
    guess=float(input())
    return guess==answer

#Creating multiple random questions
def questions():
    print("Welcome to the random equations quiz, there's going to be 10 questions. Enjoy\n")
    score=0
    for i in range(10):
        correct=askuser()
        if correct:
            score+=1
            print("You're right!\n\n")
        else:
            print("Incorrect.\n\n")
    return 'Your score is {}/10'.format(score)



def Easy():
    score=0
    
    q1=input("\n\n\nQuestion 1. What is 401 - 267?: ")
    if q1==134:
        print("That is it keep going.")
        score+=1
    elif q1 !=134:
        print("Not the right answer but you'll get there.")#yes
        

    print("\nQuestion 2. Kyle buys a pair of shoes for Â£66 and a shirt for Â£20. How much does he spend altogether?")
    print("\na)£90")
    print("b)£86")
    print("c)£83")
    a1=input("\nIs it a, b or c?: ")
    if a1==b:
        print("Well done that is indeed the right answer.")
        score+=1
    elif a1 !=b:
        print("Wrong but do not fear plenty more questions to come.")#yes
        

    q3=input("\nQuestion 3. What is 5 x 12?: ")
    if q3==60:
        print("Great you've got it!")
        score+=1
    elif q3!=60:
        print("Sorry that's not it but keep on going.")#yes


    print("\nQuestion 4. Out of 3499 and 3478, which is the bigger number?")
    print("\na)3499")
    print("b)3478")
    a2=input("\nWhich one is it?: ")
    if a2==a:
        print("Correct!")
        score+=1
    elif a2 !=a:
        print("Incorrect.")#yes


    print("\nQuestion 5. Mark has 23 Apples and his friend Julie has 19. How much does Julie have when she gives Mark 6? and how many has Mark got now? ")
    print("\nQuestion 5. A)")
    a3=input("Julie now has: ")
    if a3==13:
        print("That's right, she's now got 13 Apples left.")
        score+=1
    elif a3 !=13:
        print("Sorry you're wrong. The right answer would've been 13.")#yes

    print("\nQuestion 5. B)")
    print("How many has Mark got now after getting those 6 Apples from Julie?")
    print("\na)29")
    print("b)31")
    print("c)27")
    a4=input("\nWhat is the amount of Apples that Mark has now?: ")
    if a4==a:
        print("That's right! Mark has 29 Apples now.")
        score+=1
    elif a4 !=a:
        print("Nearly however the right answer was 29. You'll get it next time.")


    q6=input("\nQuestion 6. What is 42 / 2?: ")
    if q6==21:
        print("You're right!")
        score+=1
    elif q6 !=21:
        print("Sorry but you're wrong.")


    print("\nQuestion 7. Is it true that the number 148 is bigger than 119?")
    q7=input("\nyes or no?: ")
    if q7==yes:
        print("Right. It's indeed the bigger number.")
        score+=1
    elif q7 !=yes:
        print("The right answer would've been that it is bigger")


    print("\nQuestion 8. Write 0.40 as a percentage.")
    q8=input("\n")
    if q8==40:
        print("You're right, it's 40%")
        score+=1
    elif q8 !=40:
        print("Sorry the answer was 40%")


    q9=input("\nQuestion 9. Write two hundred thousand in figures: ")
    if q9==200000:
        print("Correct!")
        score+=1
    if q9 !=200000:
        print("Incorrect")


    print("\nQuestion 10. Work out 1433 + 217.")
    q10=input("\n")
    if q10==1450:
        print("That's right you got it.")
        score+=1
    elif q10 !=1450:
        print("Sorry that's not it.")

    print("\n\n\nCongratulations! You've scored a total of", score,"Points")


    


def Advanced():
    score=0
    
    print("\nYou chose the Advanced option, bare in mind that you might need a piece of paper and pen to solve these before picking the answer.")
    print("However if you get the answer wrong the right equation will show up so you can learn from it. Enjoy.")

    print("\n\nQuestion 1. Solve the equation 2y=6 to find the value of y.")
    print("\na)y=3")
    print("\nb)y=2")
    q1=input("\n")
    if q1==3:
        print("You got it, it's 3 indeed!")
        score+=1
    elif q1 !=3:
        print("Incorrect but have a look at how it's done. The right equation is:")
        print("\n2y/2=6/2")
        print("y=3")
    


    q2=input("\n\nQuestion 2. What is 5-0.24?: ")
    if q2==4.76:
        print("Correct.")
        score+=1
    elif q2 !=4.76:
        print("Sorry you're wrong but here's how it's done:")
        print("\n5.00")
        print("0.24")
        print("------")
        print("4.76")


    q3=input("\n\nQuestion 3. What are 5% of 500?: ")
    if q3==25:
        print("That's it!")
        score+=1
    elif q3 !=25:
        print("Wrong but you'll get there, have a look:")
        print("\n5/100*500=25")


    print("\n\nQuestion 4. Find the mean of 5,2,3,5,5,2,3,3,1,1")
    q4=input("\n")
    if q4==3:
        print("That is the mean.")
        score+=1
    elif q4 !=3:
        print("That is not the mean, have a look how it's done:")
        print("\nAdd all the numbers together.")
        print("5+2+3+5+5+2+3+3+1+1=30")
        print("\nThen count how many numbers you were given,it's 10.")
        print("30/10=3")

    
    q5=input("\n\nQuestion 5. Calculate 4+10+(5*5)-11= ")
    if q5==28:
        print("Great job.")
        score+=1
    elif q5 !=28:
        print("That's not right. Have a look:")
        print("\nYou first have to calculate whatever is in the breackets and then do the rest so this:")
        print("\n4+10+(5*5)-10 = 5*5 = 25, 25+4+10-11 = 28")
    

    print("\n\nQuestion 6. Find the median of 2,3,5,6,4,9,4,6,7")
    print("\na)7")
    print("b)9")
    print("c)5")
    q6=input("\n")
    if q6==c:
        print("You got it right.")
        score+=1
    if q6 !=c:
        print("Wrong, this is the way to do it:")
        print("\nFirst put all the numbers in order like this: 2,3,4,4,5,6,6,7,9")
        print("Then find the middle number, in this case it's 5.")
        print("Therefore the answer is answer 'c' which is 5.")
        

    print("\n\nQuestion 7. Find the mode of 2,4,5,6,4,3,4,6,1,1,4")
    print("\na)4")
    print("b)1")
    print("c)6")
    q7=input("\n")
    if q7==a:
        print("Yes the mode is indeed 4.")
        score+=1
    elif q7 !=a:
        print("Incorrect, here's how it's done:")
        print("\nFirst of all put all the numbers in an order again just like this: ")
        print("1,1,2,3,4,4,4,4,5,6,6")
        print("\nLook at which number appears the most times, in this case it's 4.")
        print("Therefore the mode is 4.")
        

    q8=input("\n\nQuestion 8. Work out 8^0= ")
    if q8==1:
        print("Correct!")
        score+=1
    elif q8 !=1:
        print("Sorry you're wrong. This is how it's done")
        print("\n8^0 = 8/8 = 1")
        

    print("\n\nQuestion 9. Which of the following numbers are written in standard index form?")
    print("\na)0.7*10^5")
    print("b)4*10^3")
    print("c)10*10^7")
    print("d)0.2*10^2")
    q9=input("\nThere's only 1 written in standard index form a,b,c or d?: ")
    if q9==b:
        print("That's right!")
        score+=1
    elif q9 !=b:
        print("Sorry wrong it was 'b', here's why:")
        print("\n'b' is written in standard index form, as 4 lies between 1 and 10.")
        print("'a' and 'd' are not written in standard index form because the value is less than 1.")
        print("Last but not least 'c' is not written in standard index form because the value 10 is not allowed.")
        

    print("\n\nQuestion 10. Solve these simultaneous equations:")
    print("\nEquation 1: 2x+y=7")
    print("Equation 2: 3x-y=8")
    q10=input("\nWhat's the answer: ")
    if q10== "x=3" and "y=7":
        print("Great!")
        score+=1
    elif q10 != "x=3" and "y=7":
        print("That's wrong. This will hopefully clear it up: ")
        print("\n\nFirst add the two equations but get rid of the y's")
        print("\n2x+y=7")
        print("3x-y=8")
        print("-----------")
        print("5x=15")
        print("x=3")
        print("\nNow we have x we can find y. We now can put x=3 in either of the equations.")
        print("\nSubsitute x=3 into the equation 2x+y=7")
        print("\n6+y=7")
        print("y=1")


    print("\n\n\nCongratulations! You've scored a total of", score,"Points")

    

def randomequations():
    questions()



beginning()
while x==0:

    again=input("\n\n\n\nWould you like to go back to the main menu and try another option? y/n?")
    if again==y:
        print("")
        beginning()
    if again !=y:
        print("\nThank you for participating. I hope you enjoyed the little test :)")
        break


    



