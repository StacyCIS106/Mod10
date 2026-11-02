def wall_square_foot(length, width, height): 
    wall_area = (2 * length * height) + (2 * width * height)
    return wall_area
def ceiling_area(length, width):
    area = length * width
    return area
user_input = input("Do you want to do this program? (yes?no): ")

while user_input.lower() == "yes":
    length = float(input("Enter the length of th room: "))
    width = float(input("Enter the width of the room: "))
    height = float(input("Enter the height of the room:"))

    wall_area = wall_square_foot(length, width, height)
    wall_gallons = wall_area / 50
    print(f"Wall Square Footage: {wall_area: .2f}")
    print(f"Gallons of paint needed for walls: {wall_gallons:.2f}")

    ceiling = ceiling_area(length, width)
    ceiling_gallons = ceiling / 50

    print(f"Ceiling square Footage: {ceiling:.2f}")
    print(f"Gallons needed for ceiling: {ceiling_gallons:.2f}")

    user_input = input("Do you want to do this program again? (yes/no): ")

print("program Ended.")
    
