from py2neo import Graph, Node, Relationship, NodeSelector

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

graph.delete_all()


a = Node('Person', name='Alice', age=21, location='广州')
b = Node('Person', name='Bob', age=22, location='上海')
c = Node('Person', name='Mike', age=21, location='北京')
r1 = Relationship(a, 'KNOWS', b)
r2 = Relationship(b, 'KNOWS', c)
graph.create(a)
graph.create(r1)
graph.create(r2)


selector = NodeSelector(graph)
print("------------> selector.select('Person', age=21)")
persons = selector.select('Person', age=21)
print(list(persons))



print("------------> selector.select('Person', age=21).limit(1)")
persons = selector.select('Person', age=21).limit(1)
print(list(persons))

print("------------> selector.select('Person')")
persons = selector.select('Person')
print(list(persons))


print("------------> selector.select('Person').where('_.name =~ \"A.*\"').first()")
persons2 = selector.select('Person').where('_.name =~ "A.*"').first()
print(persons2)

