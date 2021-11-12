hrs = input("Enter Hours:")
h = float(hrs)
r = input("Enter rate:")
rate = float(r)

if h <= 40:
	print(str(h*rate))
elif h > 40:
	print(str(40*rate+(h-40)*rate*1.5))