# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  noArgumentSpecialFunction.py
#  Last edit: 20/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.quadGenerator import quad_append
from structures.quad import Quad

def no_argument_special_function(current_program, element):
	#No pops since it has no arguments
	current_program.quad_number += quad_append(current_program, 
		Quad(current_program.quad_number, element, None, None, None))