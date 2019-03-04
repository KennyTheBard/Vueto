
from random import randint
import sys
import loader

# Commands
EXIT = "exit"
LIST = "list"
LOAD = "load"
HELP = "help"
GENERATE = "generate"

sets = loader.read_sets()

words = []
cmd = ""

def help():
	print LIST + "\t\tlist all the available word sets"
	print LOAD + " <word_set>\tload the requested load set"
	print GENERATE + "\tcreate a random word out of the previous loaded\n\t\tword set. A word set has to be already loaded."
	print EXIT + "\t\tclose the program"


def list():
	print "Available sets are:"
	for set in sets:
		print "\t" + set

def load(set):
	global words
	(words, msg) = loader.load(set)
	print msg


def generate():
	if len(words) == 0:
		print "ERROR: No set was loaded!"
		return

	wordcount = randint(2, 3)
	new_word = ""
	for i in range(wordcount):
		x = randint(0, len(words) - 1)
		new_word += words[x]

	print new_word


def interogate_user():
	sys.stdout.write(">> ")
	sys.stdout.flush()
	return sys.stdin.readline().strip('\n')


while True:
	cmd = interogate_user().lower()
	if EXIT in cmd:
		break
	elif HELP in cmd:
		help()
	elif LIST in cmd:
		list()
	elif LOAD in cmd:
		load(cmd.split(" ")[1])
	elif GENERATE in cmd:
		generate()
	else:
		print "Use <" + HELP + "> for details about how to use the program"
	print ""
