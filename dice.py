import anki_vector
import random

def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial) as robot:

		robot.behavior.say_text("Type y and I will roll a die or type n to exit")
		question = input('Would you like to roll the die [y/n]?\n')

		while question != 'n':
			if question == 'y':
				die1 = random.randint(1, 6)
				robot.behavior.say_text(str(die1))
				robot.behavior.say_text("Type y and I will roll a die or type n to exit")
				question = input('Would you like to roll the die [y/n]?\n')
			else:
				robot.behavior.say_text("Invalid response, please type y or n")
				question = input('Would you like to roll the die [y/n]?\n')

			if question =='n':
				robot.behavior.say_text("Goodbye!")

main()
