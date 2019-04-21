import io
from os import listdir
from os.path import isfile, join

def parse_word(set, word, order):
	curr = 0
	while True:
		if word[curr:curr + order] not in set:
			set[word[curr:curr + order]] = []

		if curr >= len(word) - order:
			set[word[curr:curr + order]].append("")
			break

		else:
			set[word[curr:curr + order]].append(word[curr + order])

		curr += 1



def load(my_path, order):
	set = {}
	msg = "Set loaded."

	try:
		with open(my_path, 'r') as fin:
			for line in fin:
				for word in line.strip('\n').split(" "):
					if len(word) > 0:
						parse_word(set, word.lower(), order)

	except IOError:
		msg = "File could not be opened!"

	return (set, msg)


if __name__ == "__main__":
	print load("./sets/test.txt", 1)
