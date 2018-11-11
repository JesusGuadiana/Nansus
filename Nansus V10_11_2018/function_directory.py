import json

from variable_table import VariableTable

class FunctionDirectory():

    def __init__(self):
        self.funct_list = {}

    def add_function(self, funct_name, funct_type,
            funct_param_list = [], funct_param_addresses = []):

        self.funct_list[funct_name] = {
            'name' : funct_name,
            'return_type' : funct_type,
            'return_address' : -1,
            'quadruple_number' : -1,
            'parameters' : {
                'types' : funct_param_list,
                'addresses' : funct_param_addresses,
            },
            'variables': VariableTable(),
            'number_of_local_variables' : {
                'int' : 0,
                'float' : 0,
                'char' : 0,
            },
            'number_of_temp_variables' : {
                'int' : 0,
                'float' : 0,
                'char' : 0,
            }
        }

    def has_function(self, funct_name):
        return funct_name in self.funct_list.keys()

    def get_function(self, funct_name):
        if self.has_function(funct_name):
            return self.funct_list[funct_name]
        else:
            print("No function with name " + funct_name + " exists.")
            return None

    def add_parameter_to_function(self, funct_name, type_list, addresses_list):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")
        else:          
            funct['parameters']['types'] = type_list
            funct['parameters']['addresses'] = addresses_list

    def add_variable_to_function(self, funct_name, variable_type,
            variable_name, variable_address=0):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")
        else:
            if funct['variables'].has_variable(variable_name):
                print("The variable already exists within the function.")
            else:
                funct['variables'].add_variable(variable_type, variable_name, variable_address)
                funct['number_of_local_variables'][variable_type] += 1

    def add_dimensioned_variable_to_function(self, funct_name, variable):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")            
        else:
            if funct['variables'].has_variable(variable['name']):
                print("The variable already exists within the function.")
            else:
                funct['variables'].add_dimensioned_variable(variable)
                for i in range(variable['upper_limit']):
                    funct['number_of_local_variables'][variable['type']] += 1

    def add_temporal_to_function(self, funct_name, temp_type):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")           
        else:
            funct['number_of_temp_variables'][temp_type] += 1

    def check_variable_existance(self, funct_name, variable_name):
        funct = self.get_function(funct_name)
        if funct is None:
            print("Variable " + variable_name + " already exists within this function.")          
        else:
            if funct['variables'].has_variable(variable_name):
                return True
            else:
                return False

    def get_function_type(self, funct_name):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")
        else:
            funct_type = funct['return_type']
            return funct_type

    def get_function_parameters(self, funct_name):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")            
        else:
            return funct['parameters']

    def get_function_variable(self, funct_name, variable_name):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")          
        else:
            variable = funct['variables'].get_variable(variable_name)
            if variable is None:
                #print("Variable " + variable_name + " doesn't exist in this function.")
                return None                
            else:
                return variable

    def get_function_quadruple_number(self, funct_name,):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")            
        else:
            return funct['quadruple_number']

    def set_function_quadruple_number(self, funct_name, quadruple_number):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")            
        else:
            funct['quadruple_number'] = quadruple_number

    def set_function_address(self, funct_name, address_number):
        funct = self.get_function(funct_name)
        if funct is None:
            print("No function with name " + funct_name + " exists.")            
        else:
            funct['return_address'] = address_number

    def print_directory(self):
        for funct, properties in self.funct_list.items():
            print("Function : " + str(funct))

            for prop, value in properties.items():
                if isinstance(value, VariableTable):
                    #Imprimer las variables de la lista en formato JSON estandar
                    print("  " + str(prop) + " : " +
                        json.dumps(value.variable_list, indent = 4))
                else:
                    print("  " + str(prop) + " : " + str(value))

            print("*" * 80)