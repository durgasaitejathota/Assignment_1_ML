# creating tuple containing names of brothers and sisters
brothers = ("Dundu", "Bose", "Pavan")
print("Brothers:", brothers)
sisters = ("Nikhila", "Meghana")
print("Sisters:", sisters)
# joining brothers and sisters and assigning it to siblings
siblings = sisters + brothers
print("Siblings:", siblings)
# finding length of siblings
print("Length of siblings:", len(siblings))
# modifying siblings tuple by adding father and mother and assiging it to familyMembers
family_members = ("Satyanarayana vara prasad", "Roja rani")
family_members += siblings
print("Family members:", family_members)