class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.__area = self.length * self.width
        self.__perimeter = 2 * (self.length + self.width)


    def get_area(self):
        return self.__area

    def get_perimeter(self):
        return self.__perimeter


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        self.__area = self.length * self.length
        self.__perimeter = 4 * self.length
    
    def get_area(self):
        return self.__area
    
    def get_perimeter(self):
        return self.__perimeter


# don't touch below this line


def test_rect(l, w):
    rect = Rectangle(l, w)
    print(f"Rectangle:")
    print(f" - Length: {l:.2f}")
    print(f" - Width: {w:.2f}")
    print(f" - Area: {rect.get_area():.2f}")
    print(f" - Perimeter: {rect.get_perimeter():.2f}")
    print("=====================================")


def test_square(l):
    square = Square(l)
    print(f"Square:")
    print(f" - Length: {l:.2f}")
    print(f" - Area: {square.get_area():.2f}")
    print(f" - Perimeter: {square.get_perimeter():.2f}")
    print("=====================================")


def main():
    test_rect(10.0, 5.0)
    test_rect(5.0, 10.0)
    test_square(2.0)
    test_square(7.0)


main()
