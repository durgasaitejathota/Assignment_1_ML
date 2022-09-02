it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Finding the length of the set it_companies
print("length of the set it_companies is", len(it_companies))
# Adding Twitter to the set it_companies
it_companies.add("Twitter")
print("Adding twitter:", it_companies)
# inserting new values to the set it_companies
newvalues = {'cts', 'tcs', 'infosys'}
it_companies.update(newvalues)
print("Adding multiple values:", it_companies)
# removing one value from the set
it_companies.remove('cts')
print("After removing:", it_companies)
# difference between Discord and remove
"""in Discard() if the element is present in the set then only the element is removed from the set and does not raise any exception,
 whereas in remove() method if the element is not present in the set, it raises an exception."""
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# joining set A and B
union = A.union(B)
print("Union:", union)
# Finding intersection of A and B
intersection = A.intersection(B)
print("Intersection:", intersection)
# checking whether A is subset of B
print(A.issubset(B))
# checking whether A and B are disjoint sets
print(A.isdisjoint(B))
# Joining A with B  and B with A using union funtions
C = A.union(B)
print("Joining A with B:", C)
D = B.union(A)
print("Joining B with A:", D)
# symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("symmetric_difference", symmetric_difference)
del A
del B
del it_companies
# Converting the age to a set and comparing the length of the list and the set.
set_age = set(age)
print("set age:", set_age)
print("Length of age is ", len(age))
print("Length of set_age is", len(set_age))
