# env/bin/python
import turtle
import random


def countingSort(sample):
    count = {}
    for i in sample:
        count[i] = count.get(i, 0) + 1
    return (count)


def drawCircle(countingSort, turtleHandl):
    totalFreq = 0
    ange = 0
    for x in countingSort:
        totalFreq += 1
        ange += countingSort[x]
        position = (0, 120)
    for x in countingSort:
        turtleHandl.fillcolor((random.random(),random.random(), random.random()))
        turtleHandl.begin_fill()
        turtleHandl.goto(position)
        turtleHandl.circle(-120, countingSort[x]* (360/ange))
        position = turtleHandl.position()
        turtleHandl.goto(0, 0)
        turtleHandl.end_fill()



def main():
    turtleHandl = turtle.Turtle()
    text = "hello hello  asd hi hi pi pi pi pi"
    words = text.split()
    words.sort()
    countWords = countingSort(words)
    drawCircle(countWords, turtleHandl)
    turtle.done()

if __name__ == '__main__':
    main()
