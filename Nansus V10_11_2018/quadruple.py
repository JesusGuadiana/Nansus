class Quadruple():
    
    #Constructor for the Quadruple Class, following its components as attributes
    def __init__(self, quad_num, operator, left_operand, right_operand,
            result):
        
        self.quad_num = quad_num
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    #Assign the quadruple result jump direction when necessary (GOTO's)
    def set_quad_jump(self, jump_num):
        self.result = jump_num

    #Enables string format for generated quadruple
    def __str__(self):
        return (str(self.quad_num)  + " | " + str(self.operator) + ", "
            + str(self.left_operand) + ", " + str(self.right_operand) + ", "
            + str(self.result))