#Toby Kerslake
#16-09-2014
#Variable Improvement Stretch and Challenge Excercise 1

width = float(input("Please enter the width of your garden in metres"))
length = float(input("Please enter the length of your garden in metres"))

gardenArea = length * width

gardenPerimeter = (length * 2) + (width * 2)

gardenTurfing = gardenArea - gardenPerimeter

gardenPrice = gardenTurfing * 10

print("Your garden has an area of {0} metres and a {1} metre perimeter with a 1 metre border. The total cost to turf the garden is £{2}".format(gardenArea,gardenPerimeter,gardenPrice))



