numbers = []

while True:

    snum = input("Enter a number: ")
    if snum == "done":
        break
    try:
        num = float(snum)
        numbers.append(num)
    except:
        print('Invalid input')



largest = None
smallest = None

for nums in numbers:
    if smallest is None:
        smallest = nums
    elif smallest > nums:
        smallest = nums

for nums in numbers:
    if largest is None:
        largest = nums
    elif largest < nums:
        largest = nums

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
