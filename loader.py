import io
from os import listdir
from os.path import isfile, join

STATES_FOLDER = "syllables_sets"


def load():
	syls = []
	my_path = STATES_FOLDER + "/"

	files = listdir(my_path)
	for f in files:
		with open(my_path + f, 'r') as fin:
			for line in fin:
				syls.append(line.strip('\n'))
	syls.append("")

	state_machine = []
	chances = []
	for syl in syls:
		state = []
		total = 0
		for syl in syls:
			state.append(1)
			total += 1
		chances.append(total)
		state_machine.append(state)

	return (syls, chances, state_machine)


if __name__ == "__main__":
	print load()
