import random
import anki_vector

args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:

    guessesTaken = 0

    robot.behavior.say_text('Hello! Please type in your name and hit enter')
    myName = input()

    number = random.randint(1, 20)

    robot.behavior.say_text('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

    while guessesTaken < 5:
        robot.behavior.say_text("Type a number a hit enter")
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1

        if guess == number:
            robot.behavior.say_text('Good job, ' + myName + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
            break

        if guess < number:
            robot.behavior.say_text('Your guess is too low.')

        if guess > number:
            robot.behavior.say_text('Your guess is too high.')

    if guessesTaken == 6:
        robot.behavior.say_text('Nope. The number I was thinking of was ' + str(number))
