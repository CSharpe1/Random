Pulse = int(input("How many pulses have you measured?;"))
Distance = str(input("Measured over what distance?;"))
DisType = int(input("If measurement distance was in Meter press 1\nIf measurement was in CM pres 2\n"
                    "if measurement was in inch press3\n"))

AltDistance = 1

if DisType == 1:
    print("You measured in meters")
        # Convert to 1M then convert to inchs at 39.37 inch to 1 M
    if Distance == 1:
        AltDistance = 39.37
        print(AltDistance)
    elif Distance < str(1):
 #       AltDistance = ((Distance * (1/39.37))
        print("less than 1", AltDistance)
    else :
        print("END")

elif DisType == 2:
    print("You measured in CM")
        #Convert to Meters then inchs

elif DisType == 3:

    print("Your measurment was in inchs")
        # Convert to 39.37


else:
    print("Not Valid")


PPI = Pulse / AltDistance
print("Pulse per inch = ", PPI)
DPI = int(input("What DPI do you want to print at?"))
PulsePerStroke = PPI / DPI
print("Pulse per stroke; ", PulsePerStroke)
Multiplier = 1
Divider = Multiplier * PulsePerStroke

if (Divider.is_integer()):
    print("Multiplier = ",Multiplier)
    print("Divider, =", Divider)


#
#test1 = 46.9898038103
#print((test1).is_integer())
#
