
import random as rand
import sys
import loader

# Commands
EXIT = "exit"
LIST = "list"
LOAD = "load"
HELP = "help"
GENERATE = "gen"
DEFINE = "def"

sets = loader.read_sets()

words = []
constants = {"STD_MAX": 5}
cmd = ""

def help():
	print LOAD + " <word_set> <order>\tload the requested load set"
	print GENERATE + " <max_len>\tcreate a random word out of the previous loaded\n\t\tword set. A word set has to be already loaded.\n\t\tA maximum word length must be selected."
	print EXIT + "\t\tclose the program"


def load(set):
	global words
	(words, msg) = loader.load(set)
	print msg


def generate(max_length):
	if len(words) == 0:
		print "ERROR: No set was loaded!"
		return

	wordcount = rand.randint(2, max_length)
	new_word = ""
	for i in range(wordcount):
		new_word += rand.choice(words)

	print new_word


def interogate_user():
	sys.stdout.write(">> ")
	sys.stdout.flush()
	return sys.stdin.readline().strip('\n')


while True:
	cmd = interogate_user().lower().strip().split(" ")
	if EXIT in cmd:
		break
	elif HELP in cmd:
		help()

	elif LIST in cmd:
		list()

	elif LOAD in cmd:
		load(cmd[1])
		if len(cmd) > 2:
			load(cmd[1], int(cmd[2]))
		else:
			load(cmd[1], rand.randint(2, 12))
	elif GENERATE in cmd:
		if len(cmd) > 1:
			generate(int(cmd[1]))
		else:
			generate(constants["STD_MAX"])
	elif DEFINE in cmd:
		if len(cmd) > 2:
			define(cmd[1], int(cmd[2]))
		else:
			print
	else:
		print "Use <" + HELP + "> for details about how to use the program"
	print ""
