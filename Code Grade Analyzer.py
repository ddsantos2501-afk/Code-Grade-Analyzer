# Aurthor: classmate test scores


# constants

fhours = 100
fpayrate = 75
fpaper = 50
fatempt = 25
dhours = 100
dpayrate = 75
dpaper = 50
datempt = 25
shours = 100
spayrate = 75
spaper = 50
satempt = 25
ghours = 100
gpayrate = 75
gpaper = 50
gatempt = 25

# get input

print("Name of person that we are calculating the grades for: Alex ")
fhours = float(input("Test 1: "))
fpayrate = float(input("Test 2: "))
fpaper = float(input("Test 3: "))
fatempt = float(input("Test 4: "))
print("Do you wish to Drop the lowest grade Y or N Y?")
print("Alex test is 85 is above average :B+ ")
print ("Name of person that we are calculating the grade for Alex")
dhours = float(input("Test 1: "))
dpayrate = float(input("Test 2: "))
dpaper = float(input("Test 3: "))
fatempt = float(input("Test 4: "))
print ("Do you wish to Drop the lowest Grade Y or N? Y")
print ("Alex test average is: 97")
print ("Letter Grade for the test is: A ")
print ("Name of person that we are calculating the grades for: Iccic")
shours = float(input("Test 1: "))
spayratye = float(input("Test 2: "))
spaper = float(input("Test 3: "))
satempt = float(input("Test 4: "))
print ("Do you wish to drop the lowest grade Y or N? N")
print ("Test scores must be greater than 50")
print ("Name of person that we are calculating the grade for Iccic")
ghours = float(input("Test 1: "))
gpayratye = float(input("Test 2: "))
gpaper = float(input("Test 3: "))
gatempt = float(input("Test 4: "))
print ("Do you wish to drop the lowest grade Y or N? X")
print ("Enter Y or N to drop the lowest grade.")

# Calculations
# Check for <= 30 hours

if fHouse <= fhours:
    fpayrate = fhours * fpayrate
    
# Check for <= 67 hours
elif fHours <= fhours:
    fpaper = fHours * fpayrate
    fatempt = (fhours - fhours) * (fpayrate)

# Cheack for >= 90 hours
else:
    fatempt = fHours * fpayrate
    fhours = (fhours - fhours) * (fpayrate * 4.5)
    fpayrate = (fHours - fpaper) * (fpayrate * 7.0)
