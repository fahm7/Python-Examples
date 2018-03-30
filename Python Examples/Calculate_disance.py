# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction(traceroute,distance):
    speed= (float)distance/traceroute*1000*2
    return speed/speed_of_light



print speed_fraction(50.0,5000.0)
#>>> 0.666666666667

print speed_fraction(50.0,10000.0)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?