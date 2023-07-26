'''import random

import math



# first we need to check the limit in which we are going to guess the number


lower = int(input('Enter the lower bound'))

upper = int(input('Enter the upper bound'))


x = random.randint(lower,upper)
print("\n You have only ",
          round(math.log(upper-lower+1,2)," chances to play\n")


count=0

while count < math.log(upper-lower+1) :
      guess_it = int(input())

      if x == guess_it:
          print("Congratulations! You have guessed it correct!")
          break

      elif x != guess_it:
          
                if x>guess_it:
                    print("Your number is too large. Try again")

                if x<guess_it:
                   print("Your number is too small.Try again")

           print(" You have only ", round(math.log(upper-lower+1,2) - count, " chances to play. Guess Correctly")

                 

if count >= math.log(upper-lower+1,2):
                 print("\n The number is : " x)
                 print("\n Better Luck next time")
'''

import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))
 
# Taking Inputs
upper = int(input("Enter Upper bound:- "))
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
 

                 
