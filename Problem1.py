ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorting the list
ages.sort()
print("ages=", ages)
# printing minimum value from the list
print("minimum value is", min(ages))
# printing maximum value from the list
print("maximum value is", max(ages))
# Adding minimum age to the list using insert
ages.insert(0, 19)
# Adding maximum value to the list using append
ages.append(26)
print("Adding min and max to list", ages)
# Calculating the median of the given list
import statistics
print("Median of the list", statistics.median(ages))
# Calculating the mean of the given list
Avg = sum(ages) / len(ages)
print("The avg age is:", Avg)
# Calculating the Range of ages list
RangeOfAges = max(ages) - min(ages)
print("Range of Max minus min is", RangeOfAges)