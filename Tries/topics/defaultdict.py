from collections import defaultdict



arr=['chandres','moger','shaniyar']

count=defaultdict(int)


for i in arr:
    count[i]+=1


print(count)




pairs = [("a", 1), ("b", 2), ("a", 3),("a",5)]

group=defaultdict(list)

for k,v in pairs:
    group[k].append(v)





print(group)