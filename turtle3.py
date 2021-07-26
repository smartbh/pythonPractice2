import turtle

x = input("사각형의 크기를 입력하세요")
y = input("사각형의 색을 입력하세요")

ix = int(x)


t = turtle.Turtle()
t.shape("turtle");

t.color(y)

t.forward(ix)
t.left(90)
t.forward(ix)

t.left(90)
t.forward(ix)
t.left(90)

t.forward(ix)
t.left(90)





