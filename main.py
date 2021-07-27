from turtle import Turtle, Screen
from random import randint

def main():
  #Create Turtle and Screen
  t: Turtle = Turtle()
  s: Screen = Screen()

  s.tracer(5) #controls the speed pf the render zero is instant
  s.bgcolor('black')
  t.speed(0)
  t.penup()
  t.pencolor('white')

  colors: list = ['yellow', 'red', 'cyan']

  for dot in range(500):
    #t.pendown()
    x = randint(-500, 500)
    y = randint(-500, 500)
    t.goto(x,y)
    size = randint(10,50)

    if x > -500 and x < -170:
      t.dot(size, colors[0])
    elif x>-170 and x < 170:
      t.dot(size, colors[1])
    elif x > 170:
      t.dot(size, colors[2])


    
  
  s.mainloop() #allows the screen to stay open instead of closing immediately, not necessary in repl


if __name__ == '__main__':
  main()