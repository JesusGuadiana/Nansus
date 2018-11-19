# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  gosubQuad.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
from structures.quad import Quad
from functions.quadGenerator import quad_append
import sys 

def gosub_quad(current_program, target):

	if not current_program.temporary_arg_types:
		current_program.quad_number += quad_append(current_program, Quad(current_program.quad_number, 'GOSUB', target, None,
		 current_program.func_directory.get_quad_number(target)))
		return 1
	else:
		print('Argument number mismatch at line')
		sys.exit()