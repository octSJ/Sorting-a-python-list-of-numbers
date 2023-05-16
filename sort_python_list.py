given_list1 = [5,3,0,2,4,1] #Given list

given_list2 = given_list1.copy()
min_to_max = []
max_to_min = []
for i in range(len(given_list1)):
    l1 = min(given_list1)
    min_to_max.append(l1)
    given_list1.pop(given_list1.index(l1))
for i in range(len(given_list2)):
    l2 = max(given_list2)
    max_to_min.append(l2)
    given_list2.pop(given_list2.index(l2))
print("The sorted list from lowest number to the highest : ",min_to_max)
print("The sorted list from highest number to the lowest : ",max_to_min)