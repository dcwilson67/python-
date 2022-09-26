charhrs = input("Enter Hours:")
charrate = input("Enter Pay Rate:")
hours = float(charhrs)
rate = float(charrate)

if hours <= 40:
    pay = rate * hours
else:
    pay = (rate * 40) + ((hours - 40) * (rate * 1.5))

print('Your Pay is', pay)
