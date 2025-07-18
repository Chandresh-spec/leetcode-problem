# defaultdict



from collections import defaultdict


nodes=defaultdict(set)

nodes['a'].add(1)
nodes['b'].add(2)

nodes['b'].add(3)

print(nodes)