from turtle import Turtle
#Jedo object which implements special functions
#(CIRCLE, SQUARE, RECTANGLE, FORWARD, BACK, TURNRIGHT, TURNLEFT, COLOR, ARCH, Line, thickness )
class Jedo(Turtle):

    def __init__(self, speed):
        super().__init__()
        self.speed(speed)
        self.showturtle()

    def square(self, sidesLength):
        for i in range(4):
            self.forward(sidesLength)
            self.right(90)

    def rectangle(self, xLength, yLength):
        for i in range(2):
            self.forward(xLength)
            self.turnRight(90)
            self.forward(yLength)
            self.turnRight(90)

    def triangle(self,length):
        for i in range(3):
            self.forward(length)
            self.left(120)

    def back(self, length):
        self.right(180)
        self.forward(length)

    def turnRight(self,degrees):
        self.right(degrees)

    def turnLeft(self, degrees):
        self.left(degrees)

    def thickness(self, thickness):
        self.pensize(thickness)

    def stopPen(self):
        self.penup()

    def startPen(self):
        self.pendown()

    def drawDot(self, radius, color="black"):
        self.dot(radius, color)

    def fillShape(self, color):
        self.fillcolor(color)

    def startFill(self):
        self.begin_fill()

    def stopFill(self):
        self.end_fill()

    def restart(self):
        self.reset()

    #TODO arch
    #TODO arch




# jedo = Jedo('slow');
# jedo.circle(75);
# jedo.forward(200)
# jedo.circle(75)
# jedo.circle(75, 180)
# jedo.color("red");
# jedo.pensize(25)
# jedo.forward(200);
