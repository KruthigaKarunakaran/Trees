import turtle


def draw_trunk(turt, width, height):
    turt.color('brown')
    turt.begin_fill()
    turt.setheading(0)
    turt.forward(width)
    turt.right(90)
    turt.forward(height)
    turt.right(90)
    turt.forward(width)
    turt.right(90)
    turt.forward(height)
    turt.end_fill()


def draw_tringle(turt, width, height):
    branch_overhang = height
    triangle_height = 2*height
    turt.color('green')
    turt.begin_fill()
    x_init,y_init = (turt.xcor(),turt.ycor())
    x_middle = x_init+width/2.0
    x_bottom_left = x_init - branch_overhang
    x_bottom_right = x_init + width + branch_overhang
    y_top = y_init+triangle_height

    turt.goto(x_bottom_left, y_init)
    turt.goto(x_middle, y_top)
    turt.goto(x_bottom_right, y_init)
    turt.goto(x_init,y_init)

    turt.end_fill()


def draw_leaf(turt, width, height, triangles= 3):
    for i in range(triangles):
        draw_tringle(turt, width, height)
        height_increase = height/2
        turt.sety(turt.ycor()+height_increase)


def draw_tree(turt, width, height):
    draw_trunk(turt, width, height)
    draw_leaf(turt, width, height)


turt = turtle.Turtle()
draw_tree(turt, 50, 100)
turtle.done()