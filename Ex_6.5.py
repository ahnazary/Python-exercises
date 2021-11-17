text = "X-DSPAM-Confidence:    0.8475"
pos = text.rfind(" ")
print(pos)
num = float(text[pos+1:len(text)+1])
print(num)