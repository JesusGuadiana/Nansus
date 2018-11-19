# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language VarTable Structure
#  Last edit: 18/11/2018
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
            'address' : address,
            'dimension_one' : -1,
            'dimension_two' : -1
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

    #Vector and/or matrix assignment of first dimension
    def set_dimension_one(self, identifier, value):
        if self.variable_exists(identifier):
            self.list_of_variables[identifier]['dimension_one'] = quad_number
        else:
            print ("Variable " + identifier + " does not exist in this function.")

    #Matrix assignment of second dimension
    def set_dimension_two(self, identifier, value):
        if self.variable_exists(identifier):
            self.list_of_variables[identifier]['dimension_two'] = quad_number
        else:
            print ("Variable " + identifier + " does not exist in this function.")