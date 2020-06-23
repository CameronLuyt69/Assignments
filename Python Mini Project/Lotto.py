import random

#AGE
age = int(input("Enter your age:\n"))

if age > 18:
    print("You're old enough to play")
elif age <= 17:
    print("You're not old enough to play")
    exit()

#LOTTO NUMBERS
numbers_of_lotto = []
for i in range(0,6):
    number = random.randint(1,49)

    while number in numbers_of_lotto:
        number = random.randint(1,49)

    numbers_of_lotto.append(number)

numbers_of_lotto.sort()

#USER NUMBERS
my_numbers = []
for i in range(0,6):
    number = int(input("Enter your number between 1 and 49:"))
    while (number < 1) or (number > 49):
        number = int(input("Please try again: Enter a number between 1 and 49:"))
    my_numbers.append(number)

my_numbers.sort()

count = 0
for number in my_numbers:
    if number in numbers_of_lotto:
        count += 1

#REWARDS
def c_function(count):
    if count == 2:
        value = 20,000
    elif count == 3:
        value = 100,50
    elif count == 4:
        value = 2,384,00
    elif count == 5:
        value = 8,584,00
    elif count == 6:
        value = 10,000,000,00
    return value

#RECEIPT
file = open("Slip.txt","w")

file.write(str("Players age is:"))
file.write(str(age) + '\n')
file.write(str("Today's lotto numbers") + '\n')
file.write(str(numbers_of_lotto) + '\n')
file.write(str("The numbers you picked for today's lotto:") + '\n')
file.write(str(my_numbers) + '\n')

file.write(str("You have guessed" + " " + str(count) + " " + "number(s) correctly ") + '\n')
file.write(str(c_function(count)))
file.close()