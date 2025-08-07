import math
def calculate_area(shape, dim1, dim2):
    if shape.lower() == "rectangle":
        if dim1 is None or dim2 is None:
            raise ValueError("Both dimensions are required for rectangle.")
        width, height = dim1, dim2
        return width * height
    elif shape.lower() == "triangle":
        if dim1 is None or dim2 is None:
            raise ValueError("Both dimensions are required for triangle.")
        base, height = dim1, dim2
        return 0.5 * base * height
    elif shape.lower() == "circle":
        if dim1 is None:
            raise ValueError("Dimension is required for circle.")
        radius = dim1
        return math.pi * (radius ** 2)
    else:
        raise ValueError("Please provide shape and dimensions in the correct format.")

shape = input("Enter the shape (rectangle, triangle, circle): ").strip().lower()

if shape not in ["rectangle", "triangle", "circle"]:
    print("Invalid shape. Please enter 'rectangle', 'triangle', or 'circle'.")
else:
    if shape == "rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(f"The area of the rectangle is {calculate_area(shape, width, height)}")
    elif shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"The area of the triangle is {calculate_area(shape, base, height)}")
    elif shape == "circle":
        radius = float(input("Enter radius: "))
        dim2 = None
        print(f"The area of the circle is {calculate_area(shape, radius, dim2)}")