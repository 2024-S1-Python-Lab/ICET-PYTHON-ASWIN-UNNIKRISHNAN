from graphics.rectangle import area as rect_area,perimeter as rect_perimeter
l=int(input("Enter length of the rectangle"))
b=int(input("Enter breadth of the rectangle"))
print("Rectangle-Area :",rect_area(l,b))
print("Perimeter: ",rect_perimeter(l,b))


from graphics.circle import area as circ_area,perimeter as circ_perimeter
r=float(input("Enter radius of a circle"))
print("Circle -Area: ",circ_area(r))
print("Perimeter: ",circ_perimeter(r))


from graphics.graphics3d.cuboid import area as cuboid_area,perimeter as cuboid_perimeter
l=int(input("Enter the length of the cuboid: "))
b=int(input("Enter the breadth of the cuboid: "))
h=int(input("Enter the height of the cuboid: "))
print("Cunoid - Area: ",cuboid_area(l,b,h))
print("Perimeter: ",cuboid_perimeter(l,b,h))


from graphics.graphics3d.sphere import area as sphere_area,perimeter as sphere_perimeter
r=float(input("Enter radius of a Sphere"))
print("Sphere -area: ",sphere_area(r))
print("Perimeter: ",sphere_perimeter(r))
