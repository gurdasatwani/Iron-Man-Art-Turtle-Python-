import turtle

ts=turtle.Screen()
ts.bgcolor("black")

tp=turtle.Turtle()
tp.pensize(2)
tp.color("white")
tp.speed(0)


tp2=turtle.Turtle()
tp2.pensize(2)
tp2.color("white")
tp2.speed(0)


def tier(c,x,y):
	tp.penup()
	tp.goto(x=x,y=y)
	tp.pendown()
	tp.circle(c)

tier(500,0,-300)
tier(450,0,-250)

tp.penup()
tp2.penup()
tp.goto(0,-160)
tp2.goto(0,-160)

def line(t,f):
	t.pendown()
	t.forward(f)

line(tp,100)
line(tp2,-100)

def tl(t,l,f):
	t.left(l)
	t.forward(f)

def tr(t,r,f):
	t.right(r)
	t.forward(f)


tl(tp,50,200)
tl(tp2,130,200)
tl(tp,40,80)
tl(tp2,-40,80)
tr(tp,45,80)
tr(tp2,-45,80)
tl(tp,45,150)
tl(tp2,-45,150)
tl(tp,50,50)
tl(tp2,-50,50)
tp.right(50)
tp2.left(50)
tp.circle(250,90)
tp2.circle(-250,90)


def j1(t,f1,f2,f3,r1,r2):
	t.penup()
	t.goto(0,-110)
	t.pendown()
	t.forward(f1)
	t.right(r1)
	t.forward(f2)
	t.right(r2)
	t.forward(f3)

j1(tp,65,70,70,85,95)
j1(tp2,65,70,70,-85,-95)

def j2(t,f1,f2,f3,f4,f5,f6,r1,r2,r3,r4,l):
	t.penup()
	t.forward(f1)
	t.pendown()
	tl(t,l,f2)
	tr(t,r1,f3)
	tr(t,r2,f4)
	tr(t,r3,f5)
	tr(t,r4,f6)

j2(tp,90,80,130,230,15,30,20,165,90,65,70)
j2(tp2,90,80,130,230,15,30,-20,-165,-90,-65,-70)

def j3(t,f1,f2,f3,f4,f5,r1,r2,r3,l1,l2):
	t.penup()
	t.goto(0,-20)
	t.pendown()
	tr(t,r1,f1)
	tl(t,l1,f2)
	tr(t,r2,f3)
	tl(t,l2,f4)
	tr(t,r3,f5)

j3(tp,70,70,215,70,100,90,20,15,70,60)
j3(tp2,70,70,215,70,100,-90,-20,-15,-70,-60)

def cur(t,rng,r,f):
	for i in range(rng):
		tr(t,r,f)


def j4(t,l,l2,l3,lst,r1):

	for i in range(17):
		tl(t,l,1)
	
	for i in range(35):
		tl(t,lst[i%6],5)
	
	cur(t,25,l2,2)
	t.forward(80)
	t.right(r1)
	t.forward(30)
	t.left(l3)
	t.forward(50)

c=[4,-2,-1,-1,2,-2]
c1=[-4,2,1,1,-2,2]

j4(tp,10,3,50,c,60)
j4(tp2,-10,-3,-50,c1,-60)


def j5(t,r1,r2,r3,r4):
	t.penup()
	t.forward(70)
	t.pendown()
	cur(t,45,r1,2)
	tr(t,r2,20)
	t.right(r3)
	cur(t,45,r4,2)

j5(tp,1,80,70,1)
j5(tp2,-1,-80,-70,-1)

def j6(t,l1,l2,l3,l4,r1,r2,r3,lst):
	t.penup()
	t.home()
	tl(t,l1,200)
	t.right(r1)
	t.pendown()
	cur(t,45,r2,4)
	t.left(l2)

	for i in range(30):
		tl(t,lst[i%6],5)
	
	tl(t,l3,100)
	tl(t,l4,150)
	tr(t,r3,50)

j6(tp,90,40,60,110,90,-1,75,c)
j6(tp2,90,-40,-60,-110,-90,1,-75,c1)


for i in range(200):
	tp2.circle(2)