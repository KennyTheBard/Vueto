
import random as rand
import sys
import loader

# Commands
EXIT = "exit"
LOAD = "load"
HELP = "help"
GENERATE = "gen"

set = {}
cmd = ""

def help():
	print LOAD + " <word_set> <order>\tload the requested load set"
	print GENERATE + " (<repets>)\tcreate a random word out of the previous loaded\n\t\tword set. A word set has to be already loaded.\n\t\tA maximum word length must be selected."
	print EXIT + "\t\tclose the program"


def load(setname, order):
	global set
	(set, msg) = loader.load(setname, order)
	print msg


def generate():
	if len(set) == 0:
		print "ERROR: No set was loaded!"
		return

	new_word = ""
	curr = rand.choice(set.keys())
	while True:
		new_word += curr
		curr = rand.choice(set[curr])
		if curr == "":
			break

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

	elif LOAD in cmd:
		if len(cmd) > 2:
			load(cmd[1], int(cmd[2]))
		else:
			help()

	elif GENERATE in cmd:
		repets = 1
		if len(cmd) > 1:
			repets = int(cmd[1])
		for i in xrange(repets):
			generate()

	else:
		print "Use <" + HELP + "> for details about how to use the program"
	print ""
