# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  quadGenerator.py
#  Last edit: 17/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from structures.quad import Quad
from functions.printToOutputFile import print_to_output_file

def quad_append(current_program, quad):
	current_program.quad_list.append(quad)
	return 1