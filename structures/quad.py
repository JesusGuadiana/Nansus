# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language 
#  quad.py
#  Last edit: 14/11/2018
# -----------------------------------------------------------------------------

#Class Name
class Quad():
    
    #Constructor for the Quadruple Class
    def __init__(self, quad_number, operator, left_operand, right_operand,
            result):
        #Basic structure of a quadruple
        self.quad_number = quad_number
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    #Used to fill in shift actions after their stack is resolved (GOTO's)
    def set_quad_goto(self, goto):
        self.result = goto

    #Simple format for printing the generated Quadruple
    def __str__(self):
        return (str(self.quad_number)  + " | " + str(self.operator) + " "
            + str(self.left_operand) + " " + str(self.right_operand) + " "
            + str(self.result))