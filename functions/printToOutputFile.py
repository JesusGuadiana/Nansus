# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  printToOutputFile.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
import sys

def print_to_output_file(element):
	#Open file
	orig_stdout = sys.stdout
	file = open('compilerOutput.txt', 'a')
	sys.stdout = file

	#Print to File
	print(element)

	#Close file
	sys.stdout = orig_stdout
	file.close()