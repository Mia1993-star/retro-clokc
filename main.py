import time
import turtle
wn = turtle.Screen()
#Is and object to acces the window
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple Analog Clock")
wn.tracer(0)
#the tracer turns of the animation

#Create a drawing pen
pen = turtle.Turtle
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
#width of the pen that is drawing

def draw_clock(h, m, s, pen):
#does nothing on it's own
  #Draw clock face
  pen.up()
  pen.goto(0, 210)
  #goes back to the pen
  pen.setheading(180)
  pen.color("green")
  pen.pendown()
  pen.circle(210)

  #draw the lines for the time
  pen.penup()
  pen.goto(0, 0)
  pen.setheading(90)

  for _ in range(12): #the _ is a placeholder
    pen.fd(190)
    pen.pendown()
    pen.fd(20)
    pen.penup()
    pen.goto(0, 0)
    pen.rt(30) #360/12=30

  #Draw the hour hand
  pen.penup()
  pen.goto(0, 0)
  pen.color("blue")
  pen.setheading(90) #90 degrees is up
  #each hour is 30 degrees
  angle = (h/12) * 360 #this works for all possible hours
  pwn.rt(angl)
  pen.pendown()
  pen.fd(100)

  #Draw the minute hand
  pen.penup()
  pen.goto(0, 0)
  pen.color("yellow")
  pen.setheading(90) #90 degrees is up
  #each hour is 30 degrees
  angle = (m/60) * 360 
  #60 minutes
  pwn.rt(angl)
  pen.pendown() 
  pen.fd(180)

  #Draw the second hand
  pen.penup()
  pen.goto(0, 0)
  pen.color("red")
  pen.setheading(90) #90 degrees is up
  #each hour is 30 degrees
  angle = (s/60) * 360 
  #60 seconds
  pwn.rt(angl)
  pen.pendown() 
  pen.fd(60)

while True:
  h = int(time.strftime("%I"))
  #h gives us string formated time/convert time to a string 
  m = int(time.strftime("%M"))
  s = int(time.strftime("%S"))

  
  draw_clock(h, m, s, pen) #matches up with h m s using the pen
  #needs to call the def function
  wn.update()
  #draws everything into memory
  time.sleep(1) 
  #delays the excecution
  
  pen.clear()

wn.mainloop()
#need to be because window would close otherwise

#angle=(h/12)*360+(m/60)*30
#angle=(m/60)*360+(s/60)*6
#for smoother movement
