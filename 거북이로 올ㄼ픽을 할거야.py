import turtle
t=turtle.Turtle()
c=['Red','Blue','Yellow','Green','Black']
##   0     1        2       3       
t.pensize(10)
t.color("%s"%c[1])
t.circle(40)
###########
t.penup()
t.goto(100,0)
t.pendown()
t.color("%s"%c[4])
t.circle(40)
############
t.penup()
t.goto(200,0)
t.pendown()
t.color("%s"%c[0])
t.circle(40)
###########
t.penup()
t.goto(50,-50)
t.pendown()
t.color("%s"%c[2])
t.circle(40)
########
t.penup()
t.goto(150,-50)
t.pendown()
t.color("%s"%c[3])
t.circle(40)
###########
turtle.done
