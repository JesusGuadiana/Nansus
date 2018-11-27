# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language 
#  semCube.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------

#Class Name
class SemanticCube() :

    #Defines resulting type of binary operations amongst the available types (int, float, char)
    def __init__(self) :
        self.semantic_cube = {

        #Integer interactions with:
            "int" : {

            #Integers
                "int" : {
                    "+" : "int",
                    "-" : "int",
                    "/" : "int",
                    "*" : "int",
                    "=" : "int",
                    "<" : "bool",
                    ">" : "bool",
                    "==" : "bool",
                    "<=" : "bool",
                    ">=" : "bool",
                    "!=" : "bool",
                    "&&" : "error",
                    "||" : "error"
                },

            #Floating Point Numbers
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "/" : "float",
                    "*" : "float",
                    "=" : "float",
                    "<" : "bool",
                    ">" : "bool",
                    "==" : "bool",
                    "<=" : "bool",
                    ">=" : "bool",
                    "!=" : "bool",
                    "&&" : "error",
                    "||" : "error"
                },

            #Characters
                "char" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },

            #Booleans
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "bool",
                    "||" : "bool"
                }},

        #Character interactions with:
            "char" : {

            #Integers
                "int" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },

            #Floating Point Numbers
                "float" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },

            #Characters
                "char" : {
                    "+" : "char",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "char",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },

            #Booleans
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "bool",
                    "||" : "bool"
                }},

        #Floating Point Number interactions with:
            "float" : {

            #Integers
                "int" : {
                    "+" : "float",
                    "-" : "float",
                    "/" : "float",
                    "*" : "float",
                    "=" : "float",
                    "<" : "bool",
                    ">" : "bool",
                    "==" : "bool",
                    "<=" : "bool",
                    ">=" : "bool",
                    "!=" : "bool",
                    "&&" : "error",
                    "||" : "error"
                },

            #Floating Point Numbers
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "/" : "float",
                    "*" : "float",
                    "=" : "float",
                    "<" : "bool",
                    ">" : "bool",
                    "==" : "bool",
                    "<=" : "bool",
                    ">=" : "bool",
                    "!=" : "bool",
                    "&&" : "error",
                    "||" : "error"
                },

            #Characters
                "char" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },

            #Booleans
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "bool",
                    "||" : "bool"
                }},

        #Boolean interactions with:
            "bool" : {

            #Integers
                "int" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },

            #Floating Point Numbers
                "float" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },

            #Characters
                "char" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },

            #Booleans
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "/" : "error",
                    "*" : "error",
                    "=" : "error",
                    "<" : "error",
                    ">" : "error",
                    "==" : "error",
                    "<=" : "error",
                    ">=" : "error",
                    "!=" : "error",
                    "&&" : "bool",
                    "||" : "bool"
                }}    
            }


    def get_type(self, left_operand, right_operand, operator):
        return self.semantic_cube[left_operand][right_operand][operator]