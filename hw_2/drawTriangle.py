# env/bin/python

import turtle

def drawTriangle(points,drowTurtle):
    drowTurtle.up()
    drowTurtle.goto(points[0][0],points[0][1])
    drowTurtle.down()
    drowTurtle.goto(points[1][0],points[1][1])
    drowTurtle.goto(points[2][0],points[2][1])
    drowTurtle.goto(points[0][0],points[0][1])
    drowTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,drowTurtle):

    drawTriangle(points,drowTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, drowTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, drowTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, drowTurtle)

def main():
    drowTurtle = turtle.Turtle()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    sierpinski(myPoints,5,drowTurtle)



if __name__ == "__main__":
    main()