Turtle!
============

Turtle graphics is a term for a method of programming vector graphics using a cursor (the "turtle") on a Cartesian plane. The `turtle module <http://docs.python.org/library/turtle.html>`_ is Python's implementation of this method. 

Exercise 0
-----------

In gedit, type the following code into a new document and save it as turtle1.py:

..  code-block:: python

    import turtle

    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)    
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.exitonclick()

Run turtle1.py using the CLI. A "Python Turtle Graphics" window should pop up and you should see an animation resulting in a black outlined square with sides that are 25 pixels long. Click inside the window and it should close - this is because of the line ``turtle.exitonclick()`` in your program. Comment out this line and run the program again. Is it clear why having this line in the code is pretty handy?

**Extra Credit**: Modify turtle1.py so that the box is a different color. Make the program draw a bigger or smaller square.

Exercise 1
-----------

Now we will make the code from Exercise 0 a little less tedious to write and more extensible. In gedit, type the following code into a new document and save it as turtle2.py:

..  code-block:: python

    import turtle
    
    def left_square():
        n = 4
        while n:
            turtle.left(90)
            turtle.forward(25)
            n = n-1
        turtle.exitonclick()
        
    left_square()

When you run turtle2.py from the CLI, it should look just like it did when you ran turtle1.py. Let's change the ``left_square()`` function so that it can make a square with a user specified side length(save this as turtle3.py):

..  code-block:: python

    def left_square(length):
        n = 4
        while n:
            turtle.left(90)
            turtle.forward(length)
            n = n-1
        turtle.exitonclick()
        
    length = raw_input("How big would you like your square to be? ")
    left_square(int(length))

When you run turtle3.py, you should be asked for input: "How big would you like your square to be?" Enter in any integer you'd like (well, within reason - a huge number will take forever to draw and the graphic will overflow off the screen) and when you press enter you should see the Python Turtle Graphics window pop up and draw a square using the integer you entered to determine the length of the sides. 

**Extra Credit**: Change the above code to allow the user to enter in what color they'd like the box to be in addition to how long they want the sides. Change ``left_square()`` so it draws the right color box.

Exercise 2
----------

Play around with turtle! The `docs <http://docs.python.org/library/turtle.html>`_ will likely be helpful in this exercise. Try incorporating one new turtle function into your existing code. Try drawing different shapes. Use the interpreter to interactively take your turtle on an adventure around the screen.

**Extra Credit**: Download the `Python turtle demo <http://code.google.com/p/python-turtle-demo/>`_ and start up ``turtleDemo.py``. Play around!

