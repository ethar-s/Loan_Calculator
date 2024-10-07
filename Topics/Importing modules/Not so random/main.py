# place `import` statement at top of the program
from random  import randint

# put your code here
def number_in_range(num):
    if -100 <= num <= 100:
        return 'Correct'

n = randint(-100,101)
