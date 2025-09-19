class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height
    
    def get_amount_inside(self, shape):
        if self.width < shape.width or self.height < shape.height:
            return 0
        return (self.width // shape.width) * (self.height // shape.height)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def set_side(self, side):
        self.width = side
        self.height = side
        
    def set_width(self, width):
        self.set_side(width)
        
    def set_height(self, height):
        self.set_side(height)
        
    def __str__(self):
        return f"Square(side={self.width})"

def main():
    print("Rectangle and Square Area Calculator")
    while True:
        shape_type = input("Enter shape (rectangle/square) or 'E' to quit: ").strip().lower()
        if shape_type == 'e':
            break
        elif shape_type == "rectangle":
            try:
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                rect = Rectangle(width, height)
                print(rect)
                print(f"Area: {rect.get_area()}")
                print(f"Perimeter: {rect.get_perimeter()}")
                print(f"Diagonal: {rect.get_diagonal()}")
                print(rect.get_picture())
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif shape_type == "square":
            try:
                side = int(input("Enter the side length of the square: "))
                sq = Square(side)
                print(sq)
                print(f"Area: {sq.get_area()}")
                print(f"Perimeter: {sq.get_perimeter()}")
                print(f"Diagonal: {sq.get_diagonal()}")
                print(sq.get_picture())
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Unknown shape type. Please enter 'rectangle' or 'square'.")

if __name__ == "__main__":
    main()