from py2neo import Graph, Node, Relationship, NodeSelector

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

graph.delete_all()

a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
a['age'] = 20
b['age'] = 21

r = Relationship(a, 'KNOWS', b)
print(a, b, r)

# node = graph.find_one(label='Person')
# print(node)
# relationship = graph.match_one(rel_type='KNOWS')
# print(relationship)

d = {'name': 'Alice', 'age' : 20}

# # quote string values
# d = {k:"'{}'".format(v) if isinstance(v, basestring) else v
#                      for k,v in d.items()}

cond = ' AND '.join("p.{}={}".format(prop, value) for prop, value in d.items())

query = "MATCH (p:Person) {condition} RETURN p"
query = query.format(condition=cond)
# "MATCH (p:Person) p.age=22 AND p.name='Alice' RETURN p"
results = graph.cypher.execute(query)
print(results)


a['age'] = 20
b['age'] = 21
r['time'] = '2017/08/31'
print(a, b, r)

a.setdefault('location', '北京')
print(a)

a['location'] = '上海'
a.setdefault('location', '北京')
print(a)

data = {
    'name': 'Amy',
    'age': 21
}
a.update(data)
print(a)


print(" 取 Subgraph 的各个属性 1 ------------------------------------------")
s = a | b | r
print(s)

print(" 取 Subgraph 的各个属性 2 ------------------------------------------")
print(s.keys())
print(s.labels())
print(s.nodes())
print(s.relationships())
print(s.types())

# 另外还可以利用 & 取 Subgraph 的交集，例如：
print(" & 取 Subgraph 的交集 ------------------------------------------")
s1 = a | b | r
s2 = a | b
print(s1 & s2)

# print(" ------- find graph nodes ------------------------------------------")
# node = test_graph.find_one(label='Person')
# print(node)
# relationship = test_graph.match_one(rel_type='KNOWS')
# print(relationship)
#
# print(" & find ------------------------------------------")
# data = test_graph.run('MATCH (p:Person) RETURN p LIMIT 5')
# print(list(data))
#
# selector = NodeSelector(test_graph)
# persons = selector.select('Person').where('_.name ="Alice"')
# print(list(persons))