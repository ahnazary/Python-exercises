h = input("Inset Hours:")
hrs = float(h)
r = input("Inset rate:")
rate = float(r)

def computepay(h, r):
    if hrs <= 40:
        return str(40*rate)
    elif hrs >= 40:
        return str(40*rate + (h-40)*1.5*rate)

p = computepay(hrs, rate)
print("Pay", p)