# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language VarTable Structure
#  Last edit: 14/11/2018
# -----------------------------------------------------------------------------

#Class Name
class VarTable():

	#Base Constructor
    def __init__(self):
        self.list_of_variables = {}

    #VarTable attribute definition
    def new_variable(self, v_type, identifier, address = 0):
        self.list_of_variables[identifier] = {
            'identifier' : identifier,
            'type' : v_type,
            'address' : address
        }

    #Getter function for a single variable within the local VarTable
    #(Called from current function specified in FuncDirectory)
    def get_variable(self, identifier):
        if self.variable_exists(identifier):
            return self.list_of_variables[identifier]
        else:
            return None

    #Verification of existance/non-existance prior to interacting with specified variable    
    def variable_exists(self, identifier):
        return identifier in self.list_of_variables.keys()

    #Creates a new 1 or 2 dimension variable
    def new_variable_vector_or_matrix(self, identifier):
        self.list_of_variables[identifier['identifier']] = identifier