#number of cars available
cars = 100
#number of spaces per car
space_in_a_car = 4.0
#number of drivers available
drivers = 30
#number of passengers today
passengers = 90

#calculate the number of cars that can't be driven because we don't have drivers for them
cars_not_driven = cars - drivers
#number of cars driven, written to variable for display
cars_driven = drivers
#calculate carpool capacity based on cars available and their capacity
carpool_capacity = cars_driven * space_in_a_car
#calculate how many people we need to put in each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."