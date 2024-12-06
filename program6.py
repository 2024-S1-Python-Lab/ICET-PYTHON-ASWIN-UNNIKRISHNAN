list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
if len(list1)==len(list2):
    print("a. The lists have the same length")
else:
    print("a. The lists have the different length")
print(f"b. sum of list1:{sum(list1)} and sum of list2:{sum(list2)}")
if sum(list1)==sum(list2):
    print("The lists sum to the same value")
else:
    print("The lists do not sum to the same value")
common_values=set(list1) & set(list2)
if common_values:
    print(f"c.Common values in both list:{common_values}")
else:
    print(f"c. There are no common values in both list.")
    
