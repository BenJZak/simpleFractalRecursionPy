import turtle
tracer=turtle.Turtle()
tracer.left(90)
tracer.speed(250)

def tree(i):
    if i<10:
        return
    else:
        tracer.forward(i)
        tracer.left(30)

        #change to alter tree
        tree(3.1*i/4) 
        tracer.right(30)
        tree(3.1*i/4)
        tracer.right(30)
        tree(3.1*i/4)

        tracer.left(30)
        tracer.backward(i)


tree(100)

turtle.done()