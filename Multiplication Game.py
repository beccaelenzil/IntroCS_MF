import random

def instruction():
    print "Hi, I am Eric. Were going to practice Multiplication!"

def play():
    score = 0
    for i in range(5):
        userAnswer = -1
        factor1 = random.randint(0,15)
        factor2 = random.randint(0,15)
        correctAnswer = factor1 * factor2

        while userAnswer != correctAnswer:
            userAnswer = raw_input(" please enter the product of " + str(factor1) + " and " + str(factor2) + ":")
            correctAnswer = factor1 * factor2
            try:
                userAnswer = int(userAnswer)
                if userAnswer == correctAnswer:
                    print "correct"
                    score +=1
                    print "your score is",score
                else:
                    print "incorrect"
            except:
               print 'enter an integer'





def main():
   instruction()
   play()
main()
