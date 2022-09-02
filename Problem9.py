lbs = []
kg = []
# taking input from the user
N = int(input("Enter number of Students : "))
# converting the weights to kilograms in a separate list using Loop.
for i in range(0, N):
    A = int(input())
    lbs.append(A)
print("Students weight in lbs:", lbs)
# taking length of lbs
for i in range(len(lbs)):
    lb = 0.45359237
    # converting lbs into kgs
    B = round(lbs[i] * lb, 2)
    kg.append(B)
print("Students weight in kgs", kg)
