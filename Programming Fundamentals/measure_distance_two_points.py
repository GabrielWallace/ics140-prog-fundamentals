import math

position1 = []
position2 = []

print("***********************\n* Distance Calculator *\n***********************\n")

print("Position 1-")
position1.append(eval(input("Please enter X coordinate for Position 1: ")))
position1.append(eval(input("Please enter Y coordinate for Position 1: ")))
x1 = position1[0]
y1 = position1[1]
print("Position 1 coordinates are", position1, "X, Y respectively")
print("*****End Position 1*****")

print("\nPosition 2-")
position2.append(eval(input("Please enter the X coordinate for Position 2: ")))
position2.append(eval(input("Please enter the Y coordinate for Position 2: ")))
x2 = position2[0]
y2 = position2[1]
print("Position 2 coordinates are", position2, "X, Y respectively")
print("*****End Position 2*****\n")

print("-Distance Calculation-")
distance = ((x2 - x1) * 2) + ((y2 - y1) ** 2)
print("The distance between Position 1 and Position 2 is: [", distance,"]")