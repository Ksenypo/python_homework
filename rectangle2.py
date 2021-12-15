from rectangle import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
# print(rect1.get_area())
# print(rect2.get_area())

square1 = Square(5)
square2 = Square(10)
circle1 = Circle(3)
circle2 = Circle(1)
# print(square1.get_area_sq(), square2.get_area_sq())

figures = [rect1, rect2, square1, square2, circle1, circle2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_sq())
    elif isinstance(figure, Circle):
        print(figure.get_circle_area())
    else:
        print(figure.get_area())
