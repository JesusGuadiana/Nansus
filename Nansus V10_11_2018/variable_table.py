class VariableTable():
    
    #Constructor defines only the list of variables as main attribute within the variable table
    def __init__(self):
        self.variable_list = {}

    #Returns a boolean value
    def has_variable(self, var_name):
        return var_name in self.variable_list.keys()

    #Getter function for variables within the variable table
    def get_variable(self, var_name):
        if self.has_variable(var_name):
            return self.variable_list[var_name]
        else:
            return None

    #Function to add new variable to the variable table
    def add_variable(self, var_type, var_name,
            var_memory_address = 0):
        self.variable_list[var_name] = {
            'name' : var_name,
            'type' : var_type,
            'memory_address' : var_memory_address
        }

    #Function to add vectors/arrays/matrices
    def add_dimensioned_variable(self, var):
        self.variable_list[var['name']] = var

    #Enables string format for variable table
    def __str__(self):
        return self.variable_list