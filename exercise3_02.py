charhrs = input("Enter Hours:")
charrate = input("Enter Pay Rate:")

try:
    hours = float(charhrs)
except:
    print ("Error, please enter numeric hours")
    quit()
try:
    rate = float(charrate)
except:
    print("Error, please enter numeric rate")
    quit()

if hours <= 40:
    pay = rate * hours
else:
    pay = (rate * 40) + ((hours - 40) * (rate * 1.5))

print('Your Pay is', pay)
