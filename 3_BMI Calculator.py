Weight = float(input("Please add your Weight:"))
Height = float(input("Please add your Height:"))


BMI = Weight / (Height **2)

if BMI < 18.5:
    print("you must eat more :P ")
elif  18.5 <= BMI <= 24.9:
    print("You loog Perfekt")
elif  25 <= BMI <= 29.9:
    print("You must stop eating")
else:
    print("One step and you eat earth")
