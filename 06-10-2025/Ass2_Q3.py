gr = int(input("Enter your Grades: "))
if (90 <= gr <= 100):
    print("A Grade & Excellent")
elif (80 <= gr <= 89):
    print("B Grade & Good")
elif (70 <= gr <= 79):
    print("C Grade & Average")
elif (60 <= gr <= 69):
    print("D Grade & Needs Improvement")
elif (0 <= gr <= 60):
    print("F Grade & Failing")
else:
    print("Invalid Input")