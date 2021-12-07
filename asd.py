Weight = float(input("Weight: "))
variable = str(input("(K)g or (L)bs: "))
if variable == ("K" or "k"):
    Weight = Weight*0.453592
    print(Weight)
elif variable == ("L" or "l"):
    Weight = Weight*2.20462
    print(Weight)
else:
    print("Please input K or L command")