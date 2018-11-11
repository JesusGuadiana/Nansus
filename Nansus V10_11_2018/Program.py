from function_directory import FunctionDirectory
from cubo_semantico import SemanticCube
from memory import Memory

class Program():
    """A class that represents the program"""

    def __init__(self, global_scope = "", current_scope = ""):
        """Class constructor"""
        self.global_scope = global_scope
        self.current_scope = current_scope
        self.function_directory = FunctionDirectory()
        self.semantic_cube = SemanticCube()
        self.temp_type = ""
        self.temp_variables = []
        self.temp_parameters_names = []
        self.temp_parameters_types = []
        self.temp_arguments_types = []
        self.operand_stack = []
        self.type_stack = []
        self.operator_stack = []
        self.quad_list = []
        self.jump_list = []
        self.return_list = []
        self.temporal_variable_counter = 0
        self.quad_num = 1
        self.relational_operations = ['>', '<', '>=', '<=', '==', '!=']
        self.return_flag = False
        self.current_dimensioned_varible = {}
        self.dimensioned_varible_stack = []
        self.dimensioned_varible_flag = False
        self.negation_stack = []
        self.memory = Memory()

    def print_stacks(self):
        """Print the temporal stacks of  the program"""
        print(self.operand_stack)
        print(self.type_stack)
        print(self.operator_stack)

    def print_quads(self):
        """Print the list of quadruples"""
        for quad in self.quad_list:
            print(quad)