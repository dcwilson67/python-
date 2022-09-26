def computepay(h, r):
    if h <= 40:
        p = r * h
    else:
        p = (r * 40) + ((h - 40) * (r * 1.5))
    return p

hrs = input("Enter Hours:")
rate = input("Enter Pay Rate:")
h = float(hrs)
r = float(rate)

p = computepay(h, r)
print("Pay", p)
