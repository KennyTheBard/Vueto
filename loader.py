import io
from os import listdir
from os.path import isfile, join

def parse_word(set, word):
	curr = 0
	while True:
		prev = curr
		curr += 1

		if word[prev] not in set:
			set[word[prev]] = []

		if curr >= len(word):
			set[word[prev]].append("")
			break
		else:
			set[word[prev]].append(word[curr])



def load(my_path, order):
	set = {}
	msg = "Set loaded."

	try:
		with open(my_path, 'r') as fin:
			for line in fin:
				for word in line.strip('\n').split(" "):
					if len(word) > 0:
						parse_word(set, word)

	except IOError:
		msg = "File could not be opened!"

	return (set, msg)


if __name__ == "__main__":
	print load("./sets/test.txt", 1)
