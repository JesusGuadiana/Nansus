# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  currentProgram.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
#Packages Imported
from structures.funcDirectory import *
from structures.quad import *
from structures.semCube import *
from structures.funcDirectory import *
from memory.memoryInterface import *
from memory.memoryManager import *

#Class Name
class CurrentProgram():

    #Base Constructor
    def __init__(self):

        #Global and Local Scopes
        self.scope_g = ""
        self.scope_l = ""

        #Dimensioned variable management variables
        self.vec_mat_first_dimension = 1
        self.vec_mat_second_dimension = 1
        self.vec_mat_variable_flag = False

        #Temporary Management Attributes
        self.current_func_id = ""
        self.current_id = ""
        self.current_array_id = ""
        self.current_type = ""
        self.current_param_identifier = ""
        self.current_param_type = ""
        self.current_func_param_counter = 0
        self.param_evaluation_counter = 0
        self.current_dim = 0;
        self.temporary_arg_types = []

        #Current Program's Stacks
        self.operand_stack = []
        self.type_stack = []
        self.operator_stack = []
        self.jump_stack = []

        #Code Generation control and result variables
        self.quad_number = 1
        self.quad_list = []

        #Current Program's Structures
        self.func_directory = FuncDirectory()
        self.sem_cube = SemanticCube()
        self.mem = MemInterface()

    def print_stacks(self):
        #Print the stacks on compilation
        print(self.operand_stack)
        print(self.operator_stack)
        print(self.type_stack)

    def print_quads(self):
        #Prints quadruple list
        for quad in self.quad_list:
            print(quad)