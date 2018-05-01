from py2neo import Node, Relationship, walk

from Neo4jDemo.noe4j_common.neo4j_base import connectNeo4j

test_graph = connectNeo4j()

print("------------------------------------------------ 1 ")

a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
mike = Node('Person', name='Mike')
ab = Relationship(a, "KNOWS", b)
ac = Relationship(a, "KNOWS", mike)
w = ab + Relationship(b, "LIKES", mike) + ac
print("------------------------------------------------ 2 ")
print(w)

print("------------------------------------------------ 3 ")
for item in walk(w):
    print(item)

print("------------------------------------------------ 4 ")
print(w.start_node())
print(w.end_node())
print(w.nodes())
print(w.relationships())

print("------------------------------------------------ 5 ")




