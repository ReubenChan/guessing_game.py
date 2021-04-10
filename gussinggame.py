import random


def get_integer(prompt):
    """
    Get an integer from standard input(stdin).
    The function will continue looping,and prompting
    the user, until a valid `int`is entered

    :param prompt: The string that the user will see, when
    they`re prompted to enter the value.

    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

        print("{} is not a valid number".format(temp))


help(get_integer)
highest = 1000
answer = random.randint(1,highest)
print(answer)  # TODO: Remove after testing
guess = 0 #initilise to any number that doesn't equal the answer
print("please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guessed higher")
        else: #guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry,you have not guessed it correctly")

# if guess < answer:
#     print("please guess higher")
#     guess =int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("sorry, you have guessed not correctly")
#
# elif guess > answer:
#     print("please guess lower")
#     guess =int(input())
#     if guess == answer:
#         print("well done, you guess it")
#     else:
#         print("sorry, you have guessed not correctly")
# else:
#     print("you got it first time")


