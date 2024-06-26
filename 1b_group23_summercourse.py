# -*- coding: utf-8 -*-
"""1B-Group23-SummerCourse.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18xRzuBD44LO3apQY_saMfJ1HiNoDy_Kl

### Group 23

**First Case Study : Miles Per Gallon**

Drivers are concerned with the mileage obtained by their automobiles. One driver has kept track of several tankfuls of gasoline
by recording miles driven and gallons used for each tankful. Develop a sentinel-controlled-repetition script that prompts the
user to input the miles driven and gallons used for each tankful.
The script should calculate and display the miles per gallon obtained for each tankful. After processing all input information, the
script should calculate and display the combined miles per gallon obtained for all tankfuls (that is, total miles driven divided by
total gallons used).
"""

def main():
  #Initialize total miles and total gallons
    total_miles = 0.0
    total_gallons = 0.0

  #Looping while
    while True:
        gallons = float(input("Enter the gallons used (-1 to quit): "))  #For user input of gallons
        if gallons == -1:   #If the input is -1, it will be break the loop
            break
        miles = float(input("Enter the miles driven: "))    #For user input of miles

        tank = miles / gallons  #For calculate miles/gallons
        print(f"The miles/gallon for this tank was: {tank:.2f}")

        total_miles += miles
        total_gallons += gallons

    if total_gallons != 0:
        overall_tank = total_miles / total_gallons
        print(f"The overall average miles/gallon was: {overall_tank:.2f}")
    else:
        print("No data to calculate.")

if __name__ == "__main__":
    main()

"""**Second Case Study : A Game of Chance - Crap**

• You roll two six-sided dice, each with faces containing one, two, three, four, five and six spots, respectively.

When the dice come to rest, the sum of the spots on the two upward faces is calculated.

• If the sum is 7 or 11 on the first roll, you win. If the sum is 2, 3 or 12 on the first roll (called “craps”), you lose

(i.e., the “house” wins).

• If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your “point.” To win, you must continue

rolling the dice until you “make your point” (i.e., roll that same point value). You lose by rolling a 7 before

making your point.
"""

import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    die1, die2 = roll_dice()
    sum_dice = die1 + die2
    print(f'You rolled {die1} + {die2} = {sum_dice}')

    if sum_dice in (7, 11):
        print('You win!')
    elif sum_dice in (2, 3, 12):
        print('Craps! You lose.')
    else:
        point = sum_dice
        print(f'Your point is {point}. Keep rolling to make your point.')

        while True:
            die1, die2 = roll_dice()
            sum_dice = die1 + die2
            print(f'You rolled {die1} + {die2} = {sum_dice}')

            if sum_dice == point:
                print('You made your point! You win!')
                break
            elif sum_dice == 7:
                print('You rolled a 7. You lose.')
                break

if __name__ == "__main__":
    main()

"""**Third Case Study : COVID 19 Infection Statistic**

• (COVID-19 Infection Statistics) During the first 20 days of the COVID-19 pandemic, the number

of newly infected patients per day in a country were recorded.

• Place the following numbers in a list: 174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301,

1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342 Use the built-in functions in the statistics

module to display the following statistics concerning the infection rate: minimum, maximum,

range, mean, median, variance, and standard deviation.
"""

import statistics

# Data on the number of new patients infected every day for the first 20 days
infection_numbers = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# Calculates the requested statistics
minimum = min(infection_numbers)
maximum = max(infection_numbers)
range_infections = maximum - minimum
mean = statistics.mean(infection_numbers)
median = statistics.median(infection_numbers)
variance = statistics.variance(infection_numbers)
std_deviation = statistics.stdev(infection_numbers)

# Displays statistical results
print(f'Minimum number of infections: {minimum}')
print(f'Maximum number of infections: {maximum}')
print(f'Range of infections: {range_infections}')
print(f'Mean number of infections: {mean:.2f}')
print(f'Median number of infections: {median}')
print(f'Variance of infections: {variance:.2f}')
print(f'Standard deviation of infections: {std_deviation:.2f}')