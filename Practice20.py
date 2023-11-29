# # # List of numbers
s = 0
c = 0
while True:
    a = input(" ? (or '0' to finish):")
    if a > 0:
        s += a
        c += 1
    elif a == 0:
        break
if c > 0:
    میانگین= s / c
    print(f"میانگین of {c} numbers: {میانگین}")
else:
   print("No numbers entered.")


    
