Pulse = int(input("How many pulses have you measured?;"))
Distance = str(input("Distance in CM?;"))
DPI = int(input("What DPI do you want to print at?"))
Multiplier = 1
CM_PER_INCH = 2.54
Distance_Inch = (float(Distance) / float(CM_PER_INCH))
print("Distance in Inchs", Distance_Inch)
# I was being to complicated, all I need to do is convert input measurment 
# into inchs, then divide number of pulse by the new value...

#PPI = (Pulse / Distance_Inch)
PulsePerStroke = ((Pulse / Distance_Inch) / DPI)

while Multiplier <= 100:
    Divider = Multiplier * PulsePerStroke
    print("Multiplier:", Multiplier, "\tDivider:", round(Divider,3))
    Multiplier += 1