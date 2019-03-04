
from random import randint
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
	print LIST + "\t\tlist all the available word sets"
	print LOAD + " <word_set>\tload the requested load set"
	print GENERATE + " <max_len>\tcreate a random word out of the previous loaded\n\t\tword set. A word set has to be already loaded.\n\t\tA maximum word length must be selected."
	print EXIT + "\t\tclose the program"


def list():
	print "Available sets are:"
	for set in sets:
		print "\t" + set

def load(set):
	global words
	(words, msg) = loader.load(set)
	print msg


def generate(max_length):
	if len(words) == 0:
		print "ERROR: No set was loaded!"
		return

	wordcount = randint(2, max_length)
	new_word = ""
	for i in range(wordcount):
		x = randint(0, len(words) - 1)
		new_word += words[x]

	print new_word


def define(var_name, var_val):
	constants[var_name] = var_val
	print "Valoarea variabilei " + var_name + " a fost updatat la " + var_val

def interogate_user():
	sys.stdout.write(">> ")
	sys.stdout.flush()
	return sys.stdin.readline().strip('\n')


while True:
	cmd = interogate_user().lower().strip()
	if EXIT in cmd:
		break
	elif HELP in cmd:
		help()
	elif LIST in cmd:
		list()
	elif LOAD in cmd:
		load(cmd.split(" ")[1])
	elif GENERATE in cmd:
		if len(cmd.split(" ")) > 1:
			generate(int(cmd.split(" ")[1]))
		else:
			generate(constants["STD_MAX"])
	elif DEFINE in cmd:
		if len(cmd.split(" ")) > 2:
			define(cmd.split(" ")[1], int(cmd.split(" ")[2]))
		else:
			print
	else:
		print "Use <" + HELP + "> for details about how to use the program"
	print ""
