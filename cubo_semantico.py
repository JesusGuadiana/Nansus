class SemanticCube() :
    #Defining results between operation of the available types
    def __init__(self) :
        self.semcub = {
            "int" : {
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
                    "!=" : "bool"
                },
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
                    "!=" : "bool"
                },
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
                    "!=" : "error"
                },
            "char" : {
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
                    "!=" : "error"
                },
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
                    "!=" : "error"
                },
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
                    "!=" : "error"
                },
            "float" : {
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
                    "!=" : "bool"
                },
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
                    "!=" : "bool"
                },
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
                    "!=" : "error"
                }
            }
        }

    def get_type(self, left, right, op):
        return self.semcub[left][right][op]
